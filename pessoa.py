from pydantic import BaseModel
from typing import List


class Pessoa(BaseModel):
    id_pessoa: int | None = None
    nome: str | None = None
    sobrenome: str | None = None
    idade: int | None = None
    genero: str | None = None
    endereco: str | None = None
    telefone: str | None = None

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
}'''
