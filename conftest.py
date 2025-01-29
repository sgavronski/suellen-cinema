import pytest
import database

database.database_name = "Locadora_Test"


@pytest.fixture
def pessoa_jorge():
    pessoa = {
        "nome": "Jorge",
        "sobrenome": "Arg",
        "idade": "30",
        "genero": "M",
        "endereco": "Rua das Palmeiras",
        "telefone": "47991161402"
    }
    return pessoa

@pytest.fixture
def pessoa_paulo():
    pessoa = {
        "nome": "Paulo",
        "sobrenome": "Ferdinando",
        "idade": "34",
        "genero": "M",
        "endereco": "Rua das Arvores",
        "telefone": "49991161402"
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

@pytest.fixture
def filme_mib():
    filme = {
            "titulo": "MIB",
            "ano": "2010",
            "valor": "12",
            "genero": "Ficção-científica"
            }
    return filme


