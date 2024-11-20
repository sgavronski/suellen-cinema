from typing import List
from pydantic import BaseModel
from filme import Filme
from pessoa import Pessoa


class Locacao(BaseModel):
    id: int | None = None
    data: str | None = None
    pessoa: Pessoa | None = None
    filmes: List[Filme] | None = None

