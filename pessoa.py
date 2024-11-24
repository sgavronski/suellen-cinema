from pydantic import BaseModel


class Pessoa(BaseModel):
    id_pessoa: int | None = None
    nome: str | None = None
    sobrenome: str | None = None
    idade: int | None = None
    genero: str | None = None
    altura: float | None = None
    peso: float | None = None
    idioma: str | None = None

    def print_full_name(self):
        return f"{self.nome} {self.sobrenome}"

    def get_ideal_weight(self):
        return self.altura / self.peso
'''
Exemplo objeto:
{
	"id_pessoa":1,
	"nome":"Suellen",
    "sobrenome":"Gavronski",
    "idade":"32",
    "genero": "F",
    "altura": "1.76",
    "peso": "67",
    "idioma": "Python"
}


class Person:
    def __init__(self, name, last_name, age, gender, height, weight, language):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.language = language'''

