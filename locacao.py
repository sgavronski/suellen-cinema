from typing import List
from pydantic import BaseModel
from filme import Filme
from pessoa import Pessoa


class Locacao(BaseModel):
    id: int | None = None
    data: str | None = None
    pessoa: Pessoa | None = None
    filmes: List[Filme] | None = None

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