from typing import List
from pydantic import BaseModel
from filme import Filme
from pessoa import Pessoa


class Locacao(BaseModel):
    id: int | None = None
    data: str | None = None
    pessoa: Pessoa | None = None
    filmes: List[Filme] | None = None
    valor_locacao: float | None = None
    data_limite_entrega: str | None = None
    data_devolucao: str | None = None
    multa: float | None = None
    valor_pago: float | None = None
    forma_pagamento: str | None = None
    data_pagamento: str | None = None
    status_pagamento: str | None = None
    total_debitos: float | None = None
    status_devolucao: str | None = None


#explicação do que é from typing import List
#No exemplo abaixo, é declarada uma variável lst que é do tipo Lista e que vai ter somente valores do tipo int
#Na classe declarada acima, filmes é uma variável do tipo Lista que vai receber somente objetos da classe Filme =O
def sum_list(lst: List[int]) -> int:
    return sum(lst)

# Usage
lst = [1, 2, 3, 4, 5]
#print(sum_list(lst)) # Output: 15

#exemplo 2: como o tipo de valores é do tipo string, eu retiro a função sum (não se soma letra com números) e printo
def sum_list(lst: List[str]) -> str:
    return lst

# Usage
lst = [1, 2, 3, "i", 5]
#print(sum_list(lst)) # Output: [1, 2, 3, 'i', 5]