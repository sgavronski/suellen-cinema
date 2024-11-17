from pydantic import BaseModel


class Person(BaseModel):
    cod_person: int | None = None
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
'''
class Person:
    def __init__(self, name, last_name, age, gender, height, weight, language):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.language = language'''

