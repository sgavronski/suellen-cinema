from pydantic import BaseModel


class Person(BaseModel):
    name: str | None = None
    last_name: str | None = None
    age: int | None = None
    gender: str | None = None
    height: float | None = None
    weight: float | None = None
    language: str | None = None

    def print_full_name(self):
        return f"{self.name} {self.last_name}"

    def get_ideal_weight(self):
        return self.height / self.weight
