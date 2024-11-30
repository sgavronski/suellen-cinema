from pydantic import BaseModel



class Pagamento(BaseModel):
    id_pagamento: int | None = None
    id_pessoa: int | None = None
    debitos: float | None = None
    valorpago: float | None = None
    debitosrestantes: float | None = None
    data: str | None = None



    # Pessoa
    # Locacao
    # Valor
    # Data
    # Multas {
    #      valor
    #      filme
    #      categoria
    # }