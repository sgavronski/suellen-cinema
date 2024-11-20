import datetime
from operator import index
from typing import List
from locacao import Locacao
from pessoa import Pessoa
from filme import Filme


class Database:

    __pessoas: List[Pessoa] = [] #criação de lista chamada __people
    __filmes: List[Filme] = [] #criação de lista chamada __films
    __locacoes: List[Locacao] = []

    def pessoa_size(self) -> int:
        """
        Retorna tamanho da lista de pessoas.
        """
        return len(self.__pessoas)

    def films_size(self) -> int:
         return len(self.__filmes)

    def add_pessoa(self, person: Pessoa) -> bool:
        """
        adiciona(append) à lista __people o dado da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        self.__pessoas.append(person)
        return True

    def add_filme(self, filme: Filme) -> bool:
        if self.__verify_film(filme):
            print("Não possível adicionar o filme pois está sem título")
            return False
        else:
            self.__filmes.append(filme)
            return True


    def get_pessoa(self, index: int) -> Pessoa:
        return self.__pessoas[index]
    #self= database; retorna a pessoa que está na lista __people correspondente ao numero (index) pedido

    def get_film(self,index: int) -> Filme:
        return self.__filmes[index]


    def update_pessoa(self, person: Pessoa) -> bool:
        """
        Atualiza os dados da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        index = None
        for i in range(0, len(self.__pessoas)):
            if self.__pessoas[i].cod_person == person.cod_person:
                index = i
                break

        if index is None:
            print("Pessoa nao existe. Cancelar operacao")
            return False
        else:
            #self.__people.pop(index)
            #self.add_person(person)
            self.__pessoas[index].name = person.name
            self.__pessoas[index].age = person.age
            self.__pessoas[index].weight = person.weight
            self.__pessoas[index].height = person.height
            self.__pessoas[index].gender = person.gender
            self.__pessoas[index].language = person.language
            self.__pessoas[index].last_name = person.last_name
            return True

    def update_filme(self, filme: Filme) -> bool:

        if self.__verify_film(filme):
            return False
        index = None
        for i in range(0, len(self.__filmes)):
            if filme.cod_filme == self.__filmes[i].cod_filme:
                index = i
                break
        if index == None:
            return False
        else:
            self.__filmes[index].titulo = filme.titulo
            self.__filmes[index].valor = filme.valor
            self.__filmes[index].ano = filme.ano
            self.__filmes[index].genero = filme.genero
            return True

    def delete_pessoa(self, index: int):
        self.__pessoas.pop(index)

    def delete_film(self, index: int):
        self.__filmes.pop(index)

    def get_todas_pessoas(self) -> []:
        """
        retorna todas as pessoas que estão na lista __people
        """
        return self.__pessoas

    def get_todos_filmes(self) -> []:
        return self.__filmes

    def add_locacao(self, cod_pessoa: int, cod_filmes: []) -> bool:
        locacao = Locacao()

        # Busca pessoa.
        if cod_pessoa is None or cod_pessoa <= 0:
            print("Codigo de pessoa invalido.")
            return False

        pessoa = None
        for p in self.__pessoas:
            if p.cod_person == cod_pessoa:
                pessoa = p
                break

        if pessoa is None:
            print("Pessoa nao encontrada")
            return False

        locacao.pessoa = pessoa

        # Busca filmes
        if cod_filmes is None or len(cod_filmes) == 0:
            print("Nao tem filmes cadastrados para essa locacao.")
            return False

        filmes = []
        for cod in cod_filmes:
            for filme in self.__filmes:
                if filme.cod_filme == cod:
                    filmes.append(filme)
                    break

        locacao.filmes = filmes

        # Adiciona demais atributos
        locacao.id = len(self.__locacoes) + 1
        locacao.data = datetime.date.today()

        self.__locacoes.append(locacao)
        return True

    def get_locacao(self, id: int) -> Locacao:
        for locacao in self.__locacoes:
            if locacao.id == id:
                return locacao

        print("Locacao nao encontrada")
        return None

    def update_locacao(self, id: int, locacao: Locacao) -> bool:
        locacao_encontrada = self.get_locacao(id)
        if locacao_encontrada is None:
            return False

        locacao_encontrada.pessoa = locacao.pessoa
        locacao_encontrada.filmes = locacao.filmes

        return True

    def delete_locacao(self, id: int) -> bool:
        locacao_encontrada = self.get_locacao(id)
        if locacao_encontrada is None:
            return False

        self.__locacoes.remove(locacao_encontrada)
        return True

    def get_todas_locacoes(self) -> List[Locacao]:
        return self.__locacoes

    def __verify_person(self, person: Pessoa) -> bool:
        """
        Se o nome da Pessoa for vazio retorna TRUE.
        """
        validcode = 0
        for i in range(0, len(self.__pessoas)):
            if self.__pessoas[i].name == person.name:
                validcode = 1

        if validcode==1:
            return True
        else:
            return False


    def __verify_film(self, filme: Filme) -> bool:
        if filme.titulo == "":
            return True
        else:
            return False

