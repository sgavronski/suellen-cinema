import mysql.connector
import database
from main import app
from fastapi.testclient import TestClient


class TestMain:

    banco_de_dados = mysql.connector.connect(host="localhost",
                                             user="root",
                                             password="pudim1234",
                                             database=database.database_name)

    navegador = TestClient(app)  # simula o navegador

    def test_root(self):
        response = self.navegador.get("/")

        assert response.status_code == 200
        assert response.text == "\"Cinema Suellen UP!\""

    def test_get_pessoa(self, pessoa_jorge):
        response = self.navegador.get("/pessoa?id_pessoa=1")

        assert response.status_code == 200

        pessoa = response.json()

        assert pessoa["nome"] == "Jorge"
        assert pessoa["idade"] == 30

    def test_post_pessoa(self, pessoa_jorge):
        response = self.navegador.post("/pessoa", json=pessoa_jorge)

        assert response.text == "\"Cadastro de Jorge adicionado com sucesso\""

    # Executa no final de todos os testes.
    @classmethod
    def teardown_class(cls):
        print("Final de todos os testes.")

    # Executa no final de cada teste.
    def teardown_method(self, test_method):
        cursor = self.banco_de_dados.cursor()
        cursor.execute(f"DELETE FROM {database.database_name}.pessoas")
        self.banco_de_dados.commit()
        print("Registros deletados.")
