from pydantic import BaseModel
from typing import List


class Pessoa(BaseModel):
    id_pessoa: int | None = None
    nome: str | None = None
    sobrenome: str | None = None
    idade: int | None = None
    genero: str | None = None
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

