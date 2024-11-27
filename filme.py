from pydantic import BaseModel


class Filme(BaseModel):
    id_filme: int | None = None
    titulo: str | None = None
    ano: int | None = None
    valor: float | None = None
    genero: str | None = None
    data_ultima_locacao: str | None = None


'''
    {
        "id_filme": "1",
        "titulo": "Harry Potter",
        "ano": "2003",
        "valor": "14",
        "genero": "Fantasia"
    }'''

