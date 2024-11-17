from pydantic import BaseModel


class Filme(BaseModel):
    cod_filme: int | None = None
    titulo: str | None = None
    ano: int | None = None
    valor: float | None = None
    genero: str | None = None

'''
    {
        "cod_filme": "1"
        "titulo": "Harry Potter",
        "ano": "2003",
        "valor": "14",
        "genero": "Fantasia"
    }'''

