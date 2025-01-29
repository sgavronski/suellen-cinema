import pytest
import database

database.database_name = "Locadora_Test"


@pytest.fixture
def pessoa_jorge():
    pessoa = {
        "nome": "Jorge",
        "sobrenome": "Arg",
        "idade": "30",
        "genero": "F",
        "endereco": "Rua das Palmeiras",
        "telefone": "47991161202"
    }
    return pessoa


@pytest.fixture
def filme_harry():
    filme = {
            "titulo": "Harry Potter",
            "ano": "2010",
            "valor": "15",
            "genero": "Fantasia"
            }
    return filme


