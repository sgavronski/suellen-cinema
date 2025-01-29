import mysql.connector
import database
from conftest import pessoa_jorge
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
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]
        assert response.text == f"\"Cadastro de Jorge, código *{id}* adicionado com sucesso\""

    def test_get_pessoa(self, pessoa_jorge):
        response = self.navegador.post("/pessoa",json=pessoa_jorge)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]
        response = self.navegador.get(f"/pessoa?id_pessoa={id}")

        assert response.status_code == 200

        pessoa = response.json()
        assert pessoa["nome"] == "Jorge"
        assert pessoa["idade"] == 30

    def test_put_pessoa(self, pessoa_jorge):
        response = self.navegador.post("/pessoa", json=pessoa_jorge)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]

        pessoa = {
		    "id_pessoa": id,
		    "nome":"Antonio",
	        "sobrenome":"Sauro",
	        "idade":"32",
	        "genero": "M",
		    "endereco":"Rua das Almas",
		    "telefone":"41890943"
            }
        response = self.navegador.put("/pessoa", json=pessoa)
        assert response.status_code == 200
        assert response.text == "\"Cadastro de Antonio atualizado!\""

    def test_delete_pessoa(self, pessoa_jorge):
        response = self.navegador.post("/pessoa",json=pessoa_jorge)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]

        response = self.navegador.delete(f"/pessoa?id_pessoa={id}")
        assert response.status_code == 200


    def test_post_filme(self, filme_harry):
        response = self.navegador.post("/filme", json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]

        assert response.text == f"\"Cadastro do filme Harry Potter, código *{id}* adicionado com sucesso.\""


    def test_get_filme(self,filme_harry):
        response = self.navegador.post("/filme", json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]
        response = self.navegador.get(f"filme?id_filme={id}")
        assert response.status_code == 200

        filme = response.json()
        assert filme["titulo"] == "Harry Potter"

    def test_put_filme(self,filme_harry):
        response = self.navegador.post("/filme", json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]

        filme = {
                "id_filme": id,
                "titulo": "Arcane",
                "ano": "2024",
                "valor": "20",
                "genero": "Ficção"
                }
        response = self.navegador.put("/filme",json=filme)
        assert response.status_code == 200
        assert response.text == "\"Filme Arcane atualizado com sucesso\""

    def test_delete_filme(self, filme_harry):
        response = self.navegador.post("/filme",json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        id = response.text[id1+1:id2]

        response = self.navegador.delete(f"/filme?id_filme={id}")
        assert response.status_code == 200

    def test_post_locacao(self, pessoa_jorge, filme_harry):
        response = self.navegador.post("/pessoa",json=pessoa_jorge)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idpe = response.text[id1+1:id2]

        response = self.navegador.post("/filme", json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idfi = response.text[id1 + 1:id2]

        response = self.navegador.post(f"locacao?cod_pessoa={idpe}&cod_filmes={idfi}")
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idlo = response.text[id1 + 1:id2]
        assert response.text == f"\"Locação código *{idlo}* adicionada com sucesso\""


    def test_delete_locacao(self, pessoa_jorge, filme_harry):
        response = self.navegador.post("/pessoa",json=pessoa_jorge)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idpe = response.text[id1+1:id2]

        response = self.navegador.post("/filme", json=filme_harry)
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idfi = response.text[id1 + 1:id2]

        response = self.navegador.post(f"locacao?cod_pessoa={idpe}&cod_filmes={idfi}")
        id1 = response.text.find('*')
        id2 = response.text.rfind('*')
        idlo = response.text[id1 + 1:id2]
        assert response.text == f"\"Locação código *{idlo}* adicionada com sucesso\""

        response = self.navegador.delete(f"locacao?id={idlo}")
        assert response.status_code == 200
        assert response.text == "\"Locacao excluída com sucesso\""

    # Executa no final de todos os testes.
    @classmethod
    def teardown_class(cls):
        print("Final de todos os testes.")

    # Executa no final de cada teste.
    '''def teardown_method(self, test_method):
        cursor = self.banco_de_dados.cursor()
        cursor.execute(f"delete from pessoas where id_pessoa >0")
        cursor.execute(f"delete from filmes where id_filme >0")
        self.banco_de_dados.commit()
        print("Registros deletados.")'''
