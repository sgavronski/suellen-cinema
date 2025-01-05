import mysql.connector
import datetime
from datetime import date, datetime, timedelta
from typing import List
from locacao import Locacao
from pessoa import Pessoa
from filme import Filme
import json

database_name = "Locadora"

class Database:

    mydb = mysql.connector.connect(host="localhost", user="root", password="pudim1234", database="Locadora")

    __pessoas: List[Pessoa] = []
    __filmes: List[Filme] = []
    __locacoes: List[Locacao] = []
    __codigosdelocaçoes: List[int] = []
    __codigosdepagamentos: List[int] = []

    def __init__(self):
        cursor = self.mydb.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {database_name}.pessoas ("
                       f"id_pessoa INT AUTO_INCREMENT PRIMARY KEY, "
                       f"nome VARCHAR(30), sobrenome VARCHAR(50),"
                       f"idade INT, genero enum ('F','M'), endereco VARCHAR(70), telefone varchar(13))")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {database_name}.filmes (id_filme INT AUTO_INCREMENT PRIMARY KEY, "
                        f"titulo VARCHAR(60), ano INT, valor FLOAT, genero VARCHAR(30))")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS {database_name}.locacao (id INT NOT NULL AUTO_INCREMENT, data DATE, "
                       f"pessoa INT, filmes INT, valor_locacao FLOAT, "
                       "data_limite_entrega DATE, data_devolucao DATE, multa FLOAT, valor_pago FLOAT, "
                       "forma_pagamento VARCHAR(20), data_pagamento DATE, status_pagamento varchar(30),"
                       "total_debitos FLOAT, status_devolucao VARCHAR(30), PRIMARY KEY (id), "
                       "FOREIGN KEY (pessoa) references pessoas (id_pessoa), FOREIGN KEY (filmes) references filmes (id_filme))")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS locacaofilme (id_locacao INT, id_filme INT, FOREIGN KEY (id_locacao) "
                       f"references locacao (id), FOREIGN KEY (id_filme) references filmes (id_filme))")

        self.mydb.commit()

    def pessoa_size(self) -> int:
        return len(self.__pessoas)

    def films_size(self) -> int:
         return len(self.__filmes)

    def add_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__verifica_nome_pessoa(pessoa):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        self.__pessoas.append(pessoa)

        cursor = self.mydb.cursor()

        nome = pessoa.nome
        sobrenome = pessoa.sobrenome
        idade = pessoa.idade
        genero = pessoa.genero
        endereco = pessoa.endereco
        telefone = pessoa.telefone

        com = f"INSERT INTO Locadora.pessoas (nome, sobrenome, idade, genero, endereco, telefone) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nome,sobrenome,idade,genero,endereco,telefone)
        cursor.execute(com,val)
        self.mydb.commit()
        return True


    def adicionar_filme(self, filme: Filme) -> bool:
        if self.__verifica_titulo_filme(filme):
            print("Não foi possível adicionar o filme pois está sem título")
            return False

        cursor = self.mydb.cursor()

        titulo = filme.titulo
        ano = filme.ano
        valor = filme.valor
        genero = filme.genero

        sql = f"INSERT INTO Locadora.filmes (titulo, ano, valor, genero) VALUES (%s, %s, %s, %s)"
        val = (titulo, ano, valor, genero)
        cursor.execute(sql, val)
        self.mydb.commit()

        return True


    def buscar_pessoa(self, id_pessoa: int):
        id = id_pessoa
        cursor = self.mydb.cursor()
        cursor.execute (f"SELECT * FROM pessoas where id_pessoa = %s", (id,))
        rows = cursor.fetchall()   #rows = linhas
        print(rows)
        pessoa = Pessoa()
        for row in rows:
            pessoa.id_pessoa = row[0]
            pessoa.nome = row[1]
            pessoa.sobrenome = row[2]
            pessoa.idade = row[3]
            pessoa.genero = row[4]
            pessoa.endereco = row[5]
            pessoa.telefone = row[6]
        return pessoa

    def buscar_filme(self, id_filme: int):
        id = id_filme
        cursor = self.mydb.cursor()
        cursor.execute (f"SELECT * FROM {database_name}.filmes where id_filme = %s", (id,))
        rows = cursor.fetchall()   #rows = linhas
        filme = Filme()
        for row in rows:
            filme.id_filme = row[0]
            filme.titulo = row[1]
            filme.ano = row[2]
            filme.valor = row[3]
            filme.genero = row[4]
        return filme


    def atualizar_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__verifica_nome_pessoa(pessoa):
            return False

        id = pessoa.id_pessoa
        nome = pessoa.nome
        sobrenome = pessoa.sobrenome
        idade = pessoa.idade
        genero = pessoa.genero
        endereco = pessoa.endereco
        telefone = pessoa.telefone

        cursor = self.mydb.cursor()
        sql = f'UPDATE {database_name}.pessoas SET nome = %s, sobrenome = %s, idade = %s, genero = %s, endereco = %s, telefone = %s where id_pessoa = %s'
        val = nome, sobrenome, idade, genero, endereco, telefone, id
        cursor.execute(sql,val)
        self.mydb.commit()
        return True


    def atualizar_filme(self, filme: Filme) -> bool:
        if self.__verifica_titulo_filme(filme):
            return False

        id = filme.id_filme
        titulo = filme.titulo
        ano = filme.ano
        valor = filme.valor
        genero = filme.genero

        cursor = self.mydb.cursor()
        sql = f'UPDATE {database_name}.filmes SET titulo = %s, ano = %s, valor = %s, genero = %s where id_filme = %s'
        val = titulo, ano, valor, genero, id
        cursor.execute(sql, val)
        self.mydb.commit()
        return True


    def deletar_pessoa(self, id_pessoa: int) -> bool:
        id = id_pessoa
        cursor = self.mydb.cursor()
        sql = f'DELETE FROM {database_name}.pessoas where id_pessoa = %s'
        val = (id,)
        cursor.execute(sql, val)
        self.mydb.commit()
        return True

    def deletar_filme(self, id_filme: int) -> bool:
        id = id_filme
        cursor = self.mydb.cursor()
        cursor.execute (f'DELETE FROM {database_name}.filmes where id_filme = %s', (id,))
        self.mydb.commit()
        return True

    def get_todas_pessoas(self) -> []:
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT * FROM pessoas")
        rows = cursor.fetchall()  # rows = linhas
        allpeople = []
        for row in rows:
            pessoa = Pessoa()
            pessoa.id_pessoa = row[0]
            pessoa.nome = row[1]
            pessoa.sobrenome = row[2]
            pessoa.idade = row[3]
            pessoa.genero = row[4]
            pessoa.endereco = row[5]
            pessoa.telefone = row[6]
            print(pessoa)
            allpeople.append(pessoa)

        return allpeople

    def get_todos_filmes(self) -> []:
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT * FROM filmes")
        rows = cursor.fetchall()  # rows = linhas
        allmovies = []
        for row in rows:
            filme = Filme()
            filme.id_filme = row[0]
            filme.titulo = row[1]
            filme.ano = row[2]
            filme.valor = row[3]
            filme.genero = row[4]
            allmovies.append(filme)

        return allmovies

    def adicionar_locacao(self, cod_pessoa: int, cod_filmes: []) -> bool:
        cursor = self.mydb.cursor()

        pessoa = cod_pessoa
        filmes = cod_filmes
        datahoje = date.today()
        data_limite = datahoje + timedelta(days=3)
        multa = 0
        valor_pago = 0
        status_pag = "Em débito"

        sql = (f"INSERT INTO locacao (data,pessoa, data_limite_entrega, multa, valor_pago, status_pagamento)"
               f" VALUES (%s, %s, %s, %s, %s, %s)")
        val = (datahoje, pessoa, data_limite, multa, valor_pago, status_pag)
        cursor.execute(sql, val)

        cursor.execute("SELECT id FROM locacao ORDER BY id DESC limit 1")
        ultimoid = cursor.fetchone()

        valores_filmes = []
        soma = 0
        for f in filmes:
            cursor.execute("INSERT INTO locacaofilme (id_locacao,id_filme) VALUES (%s,%s)", (ultimoid[0], f,))
            cursor.execute("SELECT valor FROM filmes where id_filme = %s", (f,))
            valorf = cursor.fetchone()
            valores_filmes.append(valorf)

        for preco in valores_filmes:
            soma += sum(preco)

        totdeb = soma + multa
        cursor.execute("UPDATE locacao SET valor_locacao = %s, total_debitos = %s where id = %s", (soma, totdeb, ultimoid[0]))

        self.mydb.commit()
        return True


    def buscar_locacao(self, id: int):
        id_locacao = id
        cursor = self.mydb.cursor()
        cursor.execute("select * from locacao inner join locacaofilme on locacao.id = locacaofilme.id_locacao "
                       " inner join filmes on filmes.id_filme = locacaofilme.id_filme "
                       "inner join pessoas on pessoas.id_pessoa = locacao.pessoa "
                       "where locacao.id = %s", (id,))
        rows = cursor.fetchall()
        print(rows[0])
        locacao = Locacao()
        locacao.id = rows[0][0]
        locacao.data = rows[0][1]
        locacao.valor_locacao = rows[0][4]
        locacao.data_limite_entrega = rows[0][5]
        locacao.data_devolucao = rows[0][6]
        locacao.multa = rows[0][7]
        locacao.valor_pago = rows[0][8]
        locacao.forma_pagamento = rows[0][9]
        locacao.data_pagamento = rows[0][10]
        locacao.status_pagamento = rows[0][11]
        locacao.total_debitos = rows[0][12]
        locacao.status_devolucao = rows[0][13]
        pessoa = Pessoa()
        pessoa.id_pessoa = rows[0][21]
        pessoa.nome = rows[0][22]
        pessoa.sobrenome = rows[0][23]
        pessoa.idade = rows[0][24]
        pessoa.genero = rows[0][25]
        pessoa.endereco = rows[0][26]
        pessoa.telefone = rows[0][27]
        locacao.pessoa = pessoa
        filmes = []
        for row in rows:
            filme = Filme()
            filme.id_filme = row[16]
            filme.titulo = row[17]
            filme.ano = row[18]
            filme.valor = row[19]
            filme.genero = row[20]
            filmes.append(filme)
        locacao.filmes = filmes
        return locacao

    def atualizar_locacao(self, id: int, cod_pessoa: int, cod_filmes: []) -> bool:
        locacao_encontrada = self.buscar_locacao(id)
        if locacao_encontrada is None:
            return False

        if cod_pessoa is None:
            print("Pessoa não identificada")
            return False


        if locacao_encontrada.status_devolucao == "Devolvida":
            print ("Não é possível alterar a locação, pois já foi devolvida")
            return False
        if locacao_encontrada.valor_pago > 0:
            valorpago = locacao_encontrada.valor_pago
            formapag = locacao_encontrada.forma_pagamento
            datapag = locacao_encontrada.data_pagamento
        else:
            valorpago = 0
            formapag = ""
            datapag = ""

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
        locacao_encontrada.valor_locacao = valorlocacao

        if filmes is None or len(filmes)==0:
            print("Filmes não encontrados")
            return False

        locacao_encontrada.pessoa = pessoa
        locacao_encontrada.filmes = filmes

        #multa
        locacao_encontrada.multa = 0

        #valor já pago
        locacao_encontrada.valor_pago = valorpago
        locacao_encontrada.forma_pagamento = formapag
        locacao_encontrada.data_pagamento = datapag

        #debitos totais
        locacao_encontrada.total_debitos = (locacao_encontrada.multa + locacao_encontrada.valor_locacao)-locacao_encontrada.valor_pago

        #configuração da data
        data_hoje = date.today()
        data_formatada = data_hoje.strftime("%d/%m/%Y")
        locacao_encontrada.data = data_formatada
        data_limite = data_hoje + timedelta(days = 3)
        data_limite_formatada = data_limite.strftime("%d/%m/%Y")
        locacao_encontrada.data_limite_entrega = data_limite_formatada

        locacao_encontrada.status_devolucao = "Em andamento"

        if locacao_encontrada.total_debitos ==0:
            locacao_encontrada.status_pagamento = "Pago"
        else:
            locacao_encontrada.status_pagamento = "Em débito"
        return True

    def delete_locacao(self, id: int) -> bool:
        locacao_encontrada = self.buscar_locacao(id)
        if locacao_encontrada is None:
            return False

        if locacao_encontrada.status_devolucao == "Devolvida":
            print("Não é possível deletar a locação pois já foi finalizada")
            return False
        if locacao_encontrada.status_pagamento == "Pago":
            print("Não é possível deletar a locação pois já foi paga")
            return False
        if locacao_encontrada.valor_pago > 0:
            print("Não é possível deletar a locação pois já foi paga")
            return False

        self.__locacoes.remove(locacao_encontrada)
        return True

    def get_todas_locacoes(self) -> List[Locacao]:
        cursor = self.mydb.cursor()
        cursor.execute("select * from locacao inner join locacaofilme on locacao.id = locacaofilme.id_locacao "
                       "inner join filmes on filmes.id_filme = locacaofilme.id_filme "
                       "inner join pessoas on pessoas.id_pessoa = locacao.pessoa order by id")
        rows = cursor.fetchall()
        print(rows)
        qtdloc = len(rows)
        print(qtdloc)
        for row in range (0, qtdloc):

        return None

    def fazer_devolucao(self, id_locacao: int, datadevolucao: str) -> bool:
        cursor = self.mydb.cursor()

        cursor.execute("SELECT * from locacao where id = %s", (id_locacao,))
        resultado = cursor.fetchone()
        if resultado:
            print("Registro encontrado")
        else:
            print("Registro não encontrado")
            return False

        multa = 0
        cursor.execute("SELECT data_limite_entrega from locacao where id = %s", (id_locacao,))
        datalimite = cursor.fetchone()
        lim = datalimite[0]
        datadev = datetime.strptime(datadevolucao,"%d/%m/%Y")
        dev = datadev.date()
        print(lim)
        print(dev)
        diferenca = (dev-lim).days
        print(diferenca)

        if diferenca <= 0:
            multa = 0
        else:
            multa = diferenca * 5

        status = "Devolvido"

        cursor.execute("SELECT total_debitos from locacao where id = %s", (id_locacao,))
        deb = cursor.fetchone()
        debtot = deb[0] + multa
        if debtot == 0:
            statuspag = "Pago"
        else:
            statuspag = "Em débito"


        sql = "UPDATE locacao SET data_devolucao = %s, multa = %s, status_devolucao = %s, total_debitos = %s, status_pagamento = %s WHERE id = %s"
        val = dev, multa, status, debtot, statuspag, id_locacao
        cursor.execute(sql, val)
        self.mydb.commit()

        return True

        '''locacao_encontrada = self.buscar_locacao(id_locacao)
        if locacao_encontrada is None:
            return False

        multa: int = 0
        z: int
        for l in self.__locacoes:
            if l.id == id_locacao:
                data_limite_format = datetime.strptime(l.data_limite_entrega,"%d/%m/%Y")
                x = data_limite_format.date()
                l.data_devolucao = datadevolucao
                data_dev = datetime.strptime(datadevolucao,"%d/%m/%Y")
                y = data_dev.date()
                diferenca = y - x
                z = diferenca.days
                if z <= 0:
                    multa = 0
                else:
                    multa = z * 5
                l.multa = multa
                l.total_debitos = (l.multa + l.valor_locacao)-l.valor_pago
        if locacao_encontrada.total_debitos > 0:
            locacao_encontrada.status_devolucao = "Devolvida"
            locacao_encontrada.status_pagamento = "Em débito"
        else:
            locacao_encontrada.status_devolucao = "Devolvida"
        return True'''

    def efetuar_pagamento(self, id_locacao: int, forma_pagamento: str, valor_pago: float) -> bool:

        cursor = self.mydb.cursor()

        cursor.execute("SELECT * from locacao where id = %s", (id_locacao,))
        resultado = cursor.fetchone()
        if resultado:
            print("Registro encontrado")
        else:
            print("Registro não encontrado")
            return False

        cursor.execute("SELECT total_debitos FROM locacao WHERE id = %s", (id_locacao,))
        debitos = cursor.fetchone()
        debitospospag = debitos[0] - valor_pago

        if debitospospag < 0:
            return False

        if debitospospag == 0:
            statuspag = "Pago"
        else:
            statuspag = "Em débito"

        datapag = date.today()

        cursor.execute("SELECT valor_pago from locacao where id = %s", (id_locacao,))
        valor_pago_anterior = cursor.fetchone()
        valor_pago_atual = valor_pago_anterior[0] + valor_pago

        sql = "UPDATE locacao SET valor_pago = %s, forma_pagamento = %s, total_debitos = %s, status_pagamento = %s, data_pagamento = %s WHERE id = %s"
        val = valor_pago_atual,forma_pagamento,debitospospag,statuspag,datapag,id_locacao
        cursor.execute(sql,val)
        self.mydb.commit()
        return True


    def __verifica_nome_pessoa(self, pessoa: Pessoa) -> bool:
        if pessoa.nome == "" or pessoa.nome is None:
            return True
        else:
            return False

    def __verifica_codigo_pessoa(self, pessoa: Pessoa) -> bool:
        for p in self.__pessoas:
            if p.id_pessoa == pessoa.id_pessoa:
                print("Esse código de identificação já pertence a outra pessoa")
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



