from typing import List

from pydantic import BaseModel


class Locacao_Dto(BaseModel):
    cod_pessoa: int | None = None
    cod_filmes: List[int] | None = None



