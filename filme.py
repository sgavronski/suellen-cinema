from pydantic import BaseModel


class Filme(BaseModel):
    id_filme: int | None = None
    titulo: str | None = None
    ano: int | None = None
    valor: float | None = None
    genero: str | None = None


