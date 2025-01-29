import mysql.connector
import datetime
from datetime import date, datetime, timedelta
from typing import List
from locacao import Locacao
from pessoa import Pessoa
from filme import Filme

database_name = "Locadora"

class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="pudim1234")
        cursor = self.mydb.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        self.mydb.commit()

        self.mydb = mysql.connector.connect(host="localhost", user="root", password="pudim1234", database=database_name)
        cursor = self.mydb.cursor()
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

    def add_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__verifica_nome_pessoa(pessoa):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        cursor = self.mydb.cursor()

        nome = pessoa.nome
        sobrenome = pessoa.sobrenome
        idade = pessoa.idade
        genero = pessoa.genero
        endereco = pessoa.endereco
        telefone = pessoa.telefone

        cursor.execute("INSERT INTO pessoas (nome, sobrenome, idade, genero, endereco, telefone) "
                       "VALUES (%s, %s, %s, %s, %s, %s)", (nome,sobrenome,idade,genero,endereco,telefone))
        pessoa.id_pessoa = cursor.lastrowid
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

        cursor.execute("INSERT INTO filmes (titulo, ano, valor, genero) VALUES (%s, %s, %s, %s)",
                       (titulo, ano, valor, genero))
        filme.id_filme = cursor.lastrowid
        self.mydb.commit()

        return True


    def buscar_pessoa(self, id_pessoa: int):
        id = id_pessoa
        cursor = self.mydb.cursor()
        cursor.execute("SELECT count(id_pessoa) from pessoas where id_pessoa = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0] >0:
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
        else:
            return "Registro de pessoa não encontrada"


    def buscar_filme(self, id_filme: int):
        id = id_filme
        cursor = self.mydb.cursor()
        cursor.execute("SELECT count(id_filme) from filmes where id_filme = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0]>0:
            cursor.execute (f"SELECT * FROM filmes where id_filme = %s", (id,))
            rows = cursor.fetchall()   #rows = linhas
            filme = Filme()
            for row in rows:
                filme.id_filme = row[0]
                filme.titulo = row[1]
                filme.ano = row[2]
                filme.valor = row[3]
                filme.genero = row[4]
            return filme
        else:
            return "Registro de filme não encontrado"


    def atualizar_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__verifica_nome_pessoa(pessoa):
            return False

        cursor = self.mydb.cursor()

        id = pessoa.id_pessoa
        cursor.execute("SELECT count(id_pessoa) from pessoas where id_pessoa = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0] >0:
            nome = pessoa.nome
            sobrenome = pessoa.sobrenome
            idade = pessoa.idade
            genero = pessoa.genero
            endereco = pessoa.endereco
            telefone = pessoa.telefone
            cursor.execute("UPDATE pessoas SET nome = %s, sobrenome = %s, idade = %s, genero = %s, endereco = %s, "
                       "telefone = %s where id_pessoa = %s", (nome, sobrenome, idade, genero, endereco, telefone, id))
            self.mydb.commit()
            return True
        else:
            return False


    def atualizar_filme(self, filme: Filme) -> bool:
        if self.__verifica_titulo_filme(filme):
            return False

        cursor = self.mydb.cursor()
        id = filme.id_filme
        cursor.execute("SELECT count(id_filme) from filmes where id_filme = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            titulo = filme.titulo
            ano = filme.ano
            valor = filme.valor
            genero = filme.genero
            cursor.execute("UPDATE filmes SET titulo = %s, ano = %s, valor = %s, genero = %s where id_filme = %s",
                           (titulo, ano, valor, genero, id))
            self.mydb.commit()
            return True
        else:
            return False


    def deletar_pessoa(self, id_pessoa: int) -> bool:
        cursor = self.mydb.cursor()
        cursor.execute("SELECT count(id_pessoa) from pessoas where id_pessoa = %s", (id_pessoa,))
        resultado = cursor.fetchone()
        if resultado[0] > 0:
            try:
                cursor.execute ("DELETE FROM pessoas where id_pessoa = %s", (id_pessoa,))
                self.mydb.commit()
                return True
            except:
                return False
        else:
            return False

    def deletar_filme(self, id_filme: int) -> bool:
        cursor = self.mydb.cursor()
        cursor.execute("SELECT count(id_filme) from filmes where id_filme = %s", (id_filme,))
        resultado = cursor.fetchone()
        if resultado[0]>0:
            try:
                cursor.execute (f'DELETE FROM filmes where id_filme = %s', (id_filme,))
                self.mydb.commit()
                return True
            except:
                return False
        else:
            return False

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
        cursor.execute("SELECT count(id_pessoa) from pessoas where id_pessoa = %s", (pessoa,))
        resultp = cursor.fetchone()
        if resultp[0]==0:
            print('Pessoa não encontrada')
            return False
        else:
            filmes = cod_filmes
            for f in filmes:
                cursor.execute("SELECT count(id_filme) from filmes where id_filme = %s", (f,))
                resultf = cursor.fetchone()
                if resultf[0]==0:
                    print(f'Nenhum filme correspondente ao código {f} foi encontrado')
                    return False
            if len(filmes)==0:
                print('Nenhum filme adicionado')
                return False

            datahoje = date.today()
            data_limite = datahoje + timedelta(days=3)
            multa = 0
            valor_pago = 0
            status_pag = "Em débito"

            cursor.execute ("INSERT INTO locacao (data,pessoa, data_limite_entrega, multa, valor_pago, status_pagamento)"
                            "VALUES (%s, %s, %s, %s, %s, %s)", (datahoje, pessoa, data_limite, multa, valor_pago, status_pag))

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
        cursor = self.mydb.cursor()

        cursor.execute("SELECT count(id) from locacao where id = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0]>0:
            print("Registro encontrado")
        else:
            print("Registro não encontrado")
            return "Registro de locação não encontrado"

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
        cursor = self.mydb.cursor()

        cursor.execute("SELECT count(id) from locacao where id = %s", (id,))
        resultid = cursor.fetchone()
        if resultid[0] == 0:
            print('Locação não encontrada')
            return False
        else:
            cursor.execute("SELECT count(id_pessoa) from pessoas where id_pessoa = %s", (cod_pessoa,))
            resultpes = cursor.fetchone()
            if resultpes[0] == 0:
                print('Pessoa não encontrada')
                return False
            else:
                for f in cod_filmes:
                    cursor.execute("Select count(id_filme) from filmes where id_filme = %s", (f,))
                    resultfil = cursor.fetchone()
                    if resultfil[0] == 0:
                        print(f'Filme de código {f} não encontrado')
                        return False

            cursor.execute("Select status_devolucao from locacao where id = %s", (id,))
            resultstadev = cursor.fetchone()
            if resultstadev[0] == "Devolvido":
                print('Locação já devolvida')
                return False
            else:
                cursor.execute("SELECT valor_pago from locacao where id = %s", (id,))
                resultvalor = cursor.fetchone()
                if resultvalor[0] == 0:
                    cursor.execute("delete from locacaofilme where id_locacao = %s", (id,))
                    datahoje = date.today()
                    data_limite = datahoje + timedelta(days=3)
                    multa = 0
                    valor_pago = 0
                    status_pag = "Em débito"

                    valores_filmes = []
                    soma = 0
                    for f in cod_filmes:
                        cursor.execute("INSERT INTO locacaofilme (id_locacao,id_filme) VALUES (%s,%s)",
                                       (id, f,))
                        cursor.execute("SELECT valor FROM filmes where id_filme = %s", (f,))
                        valorf = cursor.fetchone()
                        valores_filmes.append(valorf)

                    for preco in valores_filmes:
                        soma += sum(preco)

                    totdeb = soma + multa
                    cursor.execute("UPDATE locacao SET pessoa = %s, status_pagamento = %s, multa = %s, valor_pago = %s, data = %s, data_limite_entrega = %s, valor_locacao = %s, total_debitos = %s where id = %s",
                                   (cod_pessoa, status_pag, multa, valor_pago, datahoje, data_limite, soma, totdeb, id))
                    self.mydb.commit()
                    return True
                else:
                    cursor.execute("delete from locacaofilme where id_locacao = %s", (id,))
                    cursor.execute("Select multa, data, data_limite_entrega from locacao where id = %s", (id,))
                    resultdados = cursor.fetchall()
                    print(resultdados)
                    datahoje = resultdados[0][1]
                    data_limite = resultdados[0][2]
                    multa = resultdados[0][0]
                    valor_pago = resultvalor[0]

                    valores_filmes = []
                    soma = 0
                    for f in cod_filmes:
                        cursor.execute("INSERT INTO locacaofilme (id_locacao,id_filme) VALUES (%s,%s)",
                                       (id, f,))
                        cursor.execute("SELECT valor FROM filmes where id_filme = %s", (f,))
                        valorf = cursor.fetchone()
                        valores_filmes.append(valorf)

                    for preco in valores_filmes:
                        soma += sum(preco)

                    totdeb = (soma + multa)-valor_pago
                    if totdeb > 0:
                        status_pag = "Em débito"
                    if totdeb == 0:
                        status_pag = "Pago"
                    if totdeb < 0:
                        status_pag = "Pago"
                        print(f'Valor da nova locação menor que o valor pago. Devolver {totdeb} reais para o cliente')
                    cursor.execute(
                        "UPDATE locacao SET pessoa = %s, status_pagamento = %s, multa = %s, valor_pago = %s, data = %s, data_limite_entrega = %s, valor_locacao = %s, total_debitos = %s where id = %s",
                        (cod_pessoa, status_pag, multa, valor_pago, datahoje, data_limite, soma, totdeb, id))
                    self.mydb.commit()
                    return True



    def delete_locacao(self, id: int) -> bool:
        cursor = self.mydb.cursor()
        cursor.execute("SELECT count(id) from locacao where id = %s", (id,))
        resultado = cursor.fetchone()
        if resultado[0]==0:
            print('Locação não encontrada')
            return False
        else:
            cursor.execute("SELECT status_devolucao from locacao where id = %s", (id,))
            status_dev = cursor.fetchone()
            print(status_dev)
            if status_dev[0] == 'Devolvido':
                print('Não é possível deletar locação. Locação já devolvida')
                return False
            cursor.execute("SELECT status_pagamento from locacao where id = %s", (id,))
            status_pag = cursor.fetchone()
            print(status_pag[0])
            if status_pag[0] == 'Pago':
                print('Não é possível deletar locação. Locação já foi paga. Pode apenas ser atualizada')
                return False
            cursor.execute("SELECT valor_pago from locacao where id = %s", (id,))
            valor_pag = cursor.fetchone()
            print(valor_pag[0])
            if valor_pag[0] > 0:
                print('Já foi recebido um valor de pagamento. Só será possível alterar a locação')
                return False
            cursor.execute("DELETE from locacaofilme where id_locacao = %s", (id,))
            cursor.execute("DELETE FROM locacao where id = %s", (id,))
            self.mydb.commit()
            return True

    def ultima_locacao(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT id FROM locacao ORDER BY id DESC limit 1")
        result = cursor.fetchone()
        idlo = result[0]
        return idlo

    def get_todas_locacoes(self) -> List[Locacao]:
        cursor = self.mydb.cursor()

        cursor.execute("select distinct id from locacao "
                       "inner join locacaofilme on locacao.id = locacaofilme.id_locacao "
                       "inner join filmes on filmes.id_filme = locacaofilme.id_filme "
                       "inner join pessoas on pessoas.id_pessoa = locacao.pessoa "
                       "order by id")
        ids = cursor.fetchall()
        print(ids)

        todas_as_locacoes = []

        locacaoatual = []

        for id in ids:
            cursor.execute("select * from locacao inner join locacaofilme on locacao.id = locacaofilme.id_locacao "
                           "inner join filmes on filmes.id_filme = locacaofilme.id_filme "
                           "inner join pessoas on pessoas.id_pessoa = locacao.pessoa where id = %s", (id[0],))
            rows = cursor.fetchall()
            cursor.execute("select count(id) from locacao "
                           "inner join locacaofilme on locacao.id = locacaofilme.id_locacao "
                           "inner join filmes on filmes.id_filme = locacaofilme.id_filme "
                           "inner join pessoas on pessoas.id_pessoa = locacao.pessoa "
                           "where id = %s", (id[0],))
            qtdlinhas = cursor.fetchone()
            print(qtdlinhas)
            filmes = []
            locacaoatual.clear()
            for row in rows:
                if id[0] == row[0]:
                    print (row)
                    locacao = Locacao()
                    locacao.id = row[0]
                    locacao.data = row[1]
                    locacao.valor_locacao = row[4]
                    locacao.data_limite_entrega = row[5]
                    locacao.data_devolucao = row[6]
                    locacao.multa = row[7]
                    locacao.valor_pago = row[8]
                    locacao.forma_pagamento = row[9]
                    locacao.data_pagamento = row[10]
                    locacao.status_pagamento = row[11]
                    locacao.total_debitos = row[12]
                    locacao.status_devolucao = row[13]
                    pessoa = Pessoa()
                    pessoa.id_pessoa = row[21]
                    pessoa.nome = row[22]
                    pessoa.sobrenome = row[23]
                    pessoa.idade = row[24]
                    pessoa.genero = row[25]
                    pessoa.endereco = row[26]
                    pessoa.telefone = row[27]
                    locacao.pessoa = pessoa
                    filme = Filme()
                    filme.id_filme = row[16]
                    filme.titulo = row[17]
                    filme.ano = row[18]
                    filme.valor = row[19]
                    filme.genero = row[20]
                    filmes.append(filme)
                    locacao.filmes = filmes
                    locacaoatual.append(locacao)
                    print(locacaoatual)
                    print(len(locacaoatual))
                    if len(locacaoatual) == qtdlinhas[0]:
                        todas_as_locacoes.append(locacao)

        print(todas_as_locacoes)
        return todas_as_locacoes

    def fazer_devolucao(self, id_locacao: int, datadevolucao: str) -> bool:
        cursor = self.mydb.cursor()

        cursor.execute("SELECT count(id) from locacao where id = %s", (id_locacao,))
        resultado = cursor.fetchone()
        if resultado[0]>0:
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


    def efetuar_pagamento(self, id_locacao: int, forma_pagamento: str, valor_pago: float) -> bool:

        cursor = self.mydb.cursor()

        cursor.execute("SELECT count(id) from locacao where id = %s", (id_locacao,))
        resultado = cursor.fetchone()
        if resultado[0]>0:
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



