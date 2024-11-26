from pydantic import BaseModel
from typing import List


class Debitos(BaseModel):
    id_pessoa: int | None = None
    debito_locacao: List | None = None



    # Pessoa
    # Locacao
    # Valor
    # Data
    # Multas {
    #      valor
    #      filme
    #      categoria
    # }