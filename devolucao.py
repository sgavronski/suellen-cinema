from pydantic import BaseModel
from typing import List
from locacao import Locacao


class Devolucao(BaseModel):
    id_locacao: int | None = None
    infos_locacao: List[Locacao] | None = None
    data_devolucao: str | None = None
    multa: float | None = None
