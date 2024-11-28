from datetime import date, datetime, timedelta
from typing import List
from debito import Devolucao
from locacao import Locacao
from pessoa import Pessoa
from filme import Filme


class Database:

    __pessoas: List[Pessoa] = []
    __filmes: List[Filme] = []
    __locacoes: List[Locacao] = []

    def pessoa_size(self) -> int:
        """
        Retorna tamanho da lista de pessoas.
        """
        return len(self.__pessoas)

    def films_size(self) -> int:
         return len(self.__filmes)

    def add_pessoa(self, pessoa: Pessoa) -> bool:
        """
        adiciona(append) à lista __people o dado da pessoa (person)
        """
        if self.__verifica_nome_pessoa(pessoa):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        if self.__verifica_codigo_pessoa(pessoa):
            print("Codigo nulo ou repetido")
            return False

        self.__pessoas.append(pessoa)
        return True

    def adicionar_filme(self, filme: Filme) -> bool:
        if self.__verifica_titulo_filme(filme):
            print("Não foi possível adicionar o filme pois está sem título")
            return False

        if self.__verifica_codigo_filme(filme):
            print ("Filme com código repetido ou nulo")
            return False

        else:
            self.__filmes.append(filme)
            return True


    def buscar_pessoa(self, id_pessoa: int) -> Pessoa | str:
        pessoa = None
        for p in self.__pessoas:
            if p.id_pessoa == id_pessoa:
                pessoa = p
                return pessoa
                break

        return f'O código de pessoa digitado não retornou nenhum resultado'


    def buscar_filme(self, id_filme: int) -> Filme | str:
        filme = None
        for f in self.__filmes:
            if f.id_filme == id_filme:
                filme = f
                return filme
                break

        return "Não foi encontrado nenhum filme com este código de identificação"


    def atualizar_pessoa(self, pessoa: Pessoa) -> bool:
        """
        Atualiza os dados da pessoa (person)
        """
        if self.__verifica_nome_pessoa(pessoa):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        if self.__verifica_codigo_pessoa(pessoa):
            print("Código inválido")
            return False

        index = None
        for i in range(0, len(self.__pessoas)):
            if self.__pessoas[i].id_pessoa == pessoa.id_pessoa:
                index = i
                break

        if index is None:
            print("Pessoa nao existe. Cancelar operacao")
            return False
        else:
            self.__pessoas[index].nome = pessoa.nome
            self.__pessoas[index].idade = pessoa.idade
            self.__pessoas[index].peso = pessoa.peso
            self.__pessoas[index].altura = pessoa.altura
            self.__pessoas[index].genero = pessoa.genero
            self.__pessoas[index].idioma = pessoa.idioma
            self.__pessoas[index].sobrenome = pessoa.sobrenome
            return True

    def atualizar_filme(self, filme: Filme) -> bool:
        if self.__verifica_titulo_filme(filme):
            return False

        index = None
        for i in range(0, len(self.__filmes)):
            if filme.id_filme == self.__filmes[i].id_filme:
                index = i
                break
        if index is None:
            return False
        else:
            self.__filmes[index].titulo = filme.titulo
            self.__filmes[index].valor = filme.valor
            self.__filmes[index].ano = filme.ano
            self.__filmes[index].genero = filme.genero
            return True

    def deletar_pessoa(self, id_pessoa: int) -> bool:
        for p in self.__pessoas:
            if p.id_pessoa == id_pessoa:
                print(id_pessoa)
                self.__pessoas.remove(p)
                return True

        return False

    def deletar_filme(self, id_filme: int) -> bool:
        for f in self.__filmes:
            if f.id_filme == id_filme:
                self.__filmes.remove(f)
                return True
                break

        return False

    def get_todas_pessoas(self) -> []:
        """
        retorna todas as pessoas que estão na lista __people
        """
        return self.__pessoas

    def get_todos_filmes(self) -> []:
        return self.__filmes

    def adicionar_locacao(self, cod_pessoa: int, cod_filmes: []) -> bool: #variáveis da classe locacao_dto
        locacao = Locacao() #criação de uma variável que vai receber os dados de uma nova locação como um objeto da classe Locacao

        # Busca pessoa.
        #if pessoa is None or pessoa <= 0:
         #   print("Codigo de pessoa invalido.")
          #  return False

        pessoa = None
        for p in self.__pessoas:            #cada p representa um objeto pessoa que vai ser checado na lista __pessoas
            if p.id_pessoa == cod_pessoa:  #se o cod_pessoa digitado equivale ao código de uma pessoa da lista:
                pessoa = p                  #o objeto pessoa p vai ser atribuído à variável pessoa e a busca para (break)
                break

        if pessoa is None:                  #se nenhuma pessoa foi encontrada no for anterior, a variável pessoa estará vazia
            print("Pessoa nao encontrada")
            return False

        locacao.pessoa = pessoa             #se foi encontrada uma pessoa, esse objeto pessoa será atribuído à variável
                                            #pessoa na classe locação
        # Busca filmes
        if cod_filmes is None or len(cod_filmes) == 0:
            print("Não foram selecionados filmes para a locação")
            return False

        filmes = []                         #uma pessoa pode alugar varios filmes, por isso cria-se uma lista
        for cod in cod_filmes:              #a variavel cod_filmes também pode conter varios codigos dos filmes locados, então pra cada um desses códigos:
            for filme in self.__filmes:     #pra cada filme presente na lista de filmes cadastrados
                if filme.id_filme == cod:  #vai ser verificado se o codigo (cod) é o mesmo do código de algum filme cadastrado
                    filmes.append(filme)    #e se for, o objeto filme vai ser adicionado à lista filmes
                    break
        print(f"lista de filmes:{filmes}")
        if len(filmes) == 0:
            print("Nenhum filme válido selecionado")
            return False

        locacao.filmes = filmes             #toda a lista de filmes adicionada será atribuida à variação filmes da classe Locacao

        # Adiciona demais atributos
        locacao.id = len(self.__locacoes) + 1
        data_hoje = date.today()
        data_formatada = data_hoje.strftime("%d/%m/%y")
        locacao.data = data_formatada
        data_limite = data_hoje + timedelta(days = 3)
        data_limite_formatada = data_limite.strftime("%d/%m/%y")
        locacao.data_limite_entrega = data_limite_formatada

        #adicionar valores de cada filme
        valoresfilmes = []
        for cod in cod_filmes:
            for f in self.__filmes:
                if f.id_filme == cod:
                    valoresfilmes.append(f.valor)
        valorlocacao = sum(valoresfilmes)
        locacao.valorlocacao = valorlocacao

        for p in self.__pessoas:
            if p.id_pessoa == cod_pessoa:
                print(p.id_pessoa)
                print(cod_pessoa)
                print(valorlocacao)
                p.debitos.append(valorlocacao)

        self.__locacoes.append(locacao)    #a partir do comento que todos as variáveis são preenchidas com dados válidos, adiciona-se
        return True                        #a locação à lista da locações e retorna True

    def buscar_locacao(self, id: int) -> Locacao:
        for locacao in self.__locacoes:
            if locacao.id == id:
                return locacao

        print("Locacao nao encontrada")
        return None

    def atualizar_locacao(self, id: int, cod_pessoa: int, cod_filmes: []) -> bool:
        locacao_encontrada = self.buscar_locacao(id)
        if locacao_encontrada is None:
            return False

        if cod_pessoa is None:
            print("Pessoa não identificada")
            return False

        valoraserexcluido = locacao_encontrada.valorlocacao
        print(f'Valor a ser excluido: {valoraserexcluido}')
        idlocador = locacao_encontrada.pessoa.id_pessoa
        print(f'Id locador: {idlocador}')


        pessoa = None
        for p in self.__pessoas:
            if p.id_pessoa == cod_pessoa:
                pessoa = p
        if pessoa is None:
            print("Código de pessoa não encontrada")
            return False

        if cod_filmes is None:
            print("Sem código de filmes")
            return False

        filmes = []
        valoresfilmes = []
        for cod in cod_filmes:
            for f in self.__filmes:
                if f.id_filme == cod:
                    filmes.append(f)
                    valoresfilmes.append(f.valor)
        valorlocacao = sum(valoresfilmes)
        locacao_encontrada.valorlocacao = valorlocacao

        if filmes is None or len(filmes)==0:
            print("Filmes não encontrados")
            return False

        locacao_encontrada.pessoa = pessoa
        locacao_encontrada.filmes = filmes
        for p in self.__pessoas:
            if p.id_pessoa == idlocador:
                print(f'Debitos do locador antigo: {p.debitos}')
                p.debitos.remove(valoraserexcluido)
                print(f'Debitos do locador antigo apos a remoção: {p.debitos}')
            if p.id_pessoa == cod_pessoa:
                p.debitos.append(valorlocacao)

        data_hoje = date.today()
        data_formatada = data_hoje.strftime("%d/%m/%y")
        locacao_encontrada.data = data_formatada
        data_limite = data_hoje + timedelta(days = 3)
        data_limite_formatada = data_limite.strftime("%d/%m/%y")
        locacao_encontrada.data_limite_entrega = data_limite_formatada

        return True

    def delete_locacao(self, id: int) -> bool:
        locacao_encontrada = self.buscar_locacao(id)
        if locacao_encontrada is None:
            return False

        #exclui o débito do locador referente à locação que será excluída
        valoraserexcluido = locacao_encontrada.valorlocacao
        print(valoraserexcluido)
        idlocador = locacao_encontrada.pessoa.id_pessoa
        print(idlocador)
        for p in self.__pessoas:
            if p.id_pessoa == idlocador:
                p.debitos.remove(valoraserexcluido)

        self.__locacoes.remove(locacao_encontrada)
        return True

    def get_todas_locacoes(self) -> List[Locacao]:
        return self.__locacoes

    def fazer_devolucao(self, id_locacao: int) -> bool:
        devolucao = Devolucao()
        locacao_encontrada = self.buscar_locacao(id_locacao)
        if locacao_encontrada is None:
            return False

        multa = 0
        for l in self.__locacoes:
            if l.id == id_locacao:
                devolucao.infos_locacao = l
                dialimite = l.data_limite_entrega
                print(dialimite)
                datadevolucao = date.today()
                datadevolucaoformatada = datadevolucao.strftime("%d/%m/%y")
                print(datadevolucaoformatada)
                diferencadias = datadevolucao - datadevolucao
                print(diferencadias)
                if diferencadias <= 0:
                    multa = 0
                    devolucao.multa = multa
                else:
                    multa = diferencadias * 3
                    devolucao.multa = multa
                print(devolucao.multa)
                idlocador = l.pessoa
                print(idlocador)

        for p in self.__pessoas:
            if p.id_pessoa == idlocador:
                p.multas.append(multa)

        return True


    def __verifica_nome_pessoa(self, pessoa: Pessoa) -> bool:
        """
        Se o nome da Pessoa for vazio retorna TRUE.
        """
        if pessoa.nome == "" or pessoa.nome is None:
            return True
        else:
            return False

    def __verifica_codigo_pessoa(self, pessoa: Pessoa) -> bool:
        for p in self.__pessoas:
            if p.id_pessoa == pessoa.id_pessoa:
                print("Não foi possível adicionar novo membro pois esse código de identificação já pertence a outra pessoa")
                return True
                break

        if pessoa.id_pessoa is None:
            print("Pessoa sem código")
            return True

        return False

    def __verifica_titulo_filme(self, filme: Filme) -> bool:
        if filme.titulo == "" or filme.titulo is None:
            return True
        else:
            return False

    def __verifica_codigo_filme(self, filme: Filme) -> bool:
        for f in self.__filmes:
            if f.id_filme == filme.id_filme:
                print("Código repetido")
                return True
                break

        if filme.id_filme is None:
            print ("Filme sem código")
            return True

        return False

