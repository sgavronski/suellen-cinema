from typing import List

from person import Person


class Database:

    __people: List[Person] = [] #criação de lista chamada __people
    __films: List[None] = []

    def people_size(self) -> int:
        """
        Retorna tamalho da lista de pessoas.
        """
        return len(self.__people)

    def add_person(self, person: Person) -> bool:
        """
        adiciona(append) à lista __people o dado da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        self.__people.append(person)
        return True

    def get_person(self, index: int) -> Person:
        return self.__people[index]
    #self= database; retorna a pessoa que está na lista __people correspondente ao numero (index) pedido

    def update_person(self, person: Person) -> bool:
        """
        Atualiza os dados da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        index = None
        for i in range(0, len(self.__people)):
            if self.__people[i].name == person.name:
                index = i
                break

        if index is None:
            print("Pessoa nao existe. Cancelar operacao")
            return False

        self.__people.pop(index)
        self.add_person(person)

        return True

    def delete_person(self, index: int):
        self.__people.pop(index)

    def get_people(self) -> []:
        """
        retorna todas as pessoas que estão na lista __people
        """
        return self.__people

    def __verify_person(self, person: Person) -> bool:
        """
        Se o nome da Pessoa for fazio retora TRUE.
        """
        return person.name is None

