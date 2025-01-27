import mysql.connector
import database
from main import app
from fastapi.testclient import TestClient


class TestMain: #ESSA É A CLASSE DE TESTES

    banco_de_dados = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="pudim1234",
                                             database=database.database_name)
    cursor = banco_de_dados.cursor()

    navegador = TestClient(app)  # simula o navegador

    def test_root(self):
        response = self.navegador.get("/")

        assert response.status_code == 200
        assert response.text == "\"Cinema Suellen UP!\""

    def test_post_pessoa(self, pessoa_jorge):
        response = self.navegador.post("/pessoa", json=pessoa_jorge)

        assert response.text == "\"Cadastro de Jorge adicionado com sucesso\""


    def test_post_filme(self, filme_harry):
        response = self.navegador.post("/filme", json=filme_harry)

        assert response.text == "\"Cadastro do filme Harry Potter adicionado com sucesso.\""

    def test_get_pessoa(self, pessoa_jorge):
        response = self.navegador.get("/pessoa?id_pessoa=1")

        assert response.status_code == 200

        pessoa = response.json()
        print(pessoa)

        assert pessoa["nome"] == "Jorge"
        assert pessoa["idade"] == 30

    '''def test_get_filme(self,filme_harry):
        response = self.navegador.get("filme?id_filme=1")
        assert response.status_code == 200

        filme = response.json()
        assert filme["titulo"] == "Harry Potter"'''



    # Executa no final de todos os testes.
    @classmethod
    def teardown_class(cls):
        print("Final de todos os testes.")

    # Executa no final de cada teste.
    '''def teardown_method(self, test_method):
        cursor = self.banco_de_dados.cursor()
        cursor.execute(f"delete from pessoas where id_pessoa >0")
        #cursor.execute(f"drop database Locadora_Test")
        self.banco_de_dados.commit()
        print("Registros deletados.")'''
