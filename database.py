from operator import index
from typing import List

from person import Person
from filme import Filme


class Database:

    __people: List[Person] = [] #criação de lista chamada __people
    __films: List[Filme] = [] #criação de lista chamada __films

    def people_size(self) -> int:
        """
        Retorna tamanho da lista de pessoas.
        """
        return len(self.__people)

    def films_size(self) -> int:
         return len(self.__films)

    def add_person(self, person: Person) -> bool:
        """
        adiciona(append) à lista __people o dado da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        self.__people.append(person)
        return True

    def add_filme(self, filme: Filme) -> bool:
        if self.__verify_film(filme):
            print("Não possível adicionar o filme pois está sem título")
            return False
        else:
            self.__films.append(filme)
            return True


    def get_person(self, index: int) -> Person:
        return self.__people[index]
    #self= database; retorna a pessoa que está na lista __people correspondente ao numero (index) pedido

    def get_film(self,index: int) -> Filme:
        return self.__films[index]


    def update_person(self, person: Person) -> bool:
        """
        Atualiza os dados da pessoa (person)
        """
        if self.__verify_person(person):
            print("Pessoa nao tem nome. Cancelar operacao")
            return False

        index = None
        for i in range(0, len(self.__people)):
            if self.__people[i].cod_person == person.cod_person:
                index = i
                break

        if index is None:
            print("Pessoa nao existe. Cancelar operacao")
            return False
        else:
            #self.__people.pop(index)
            #self.add_person(person)
            self.__people[i].name = person.name
            self.__people[i].age = person.age
            self.__people[i].weight = person.weight
            self.__people[i].height = person.height
            self.__people[i].gender = person.gender
            self.__people[i].language = person.language
            self.__people[i].last_name = person.last_name
            return True

    #def update_film(self, filme: Filme) -> bool:

    def delete_person(self, index: int):
        self.__people.pop(index)

    def delete_film(self, index: int):
        self.__films.pop(index)

    def get_people(self) -> []:
        """
        retorna todas as pessoas que estão na lista __people
        """
        return self.__people

    def getallmovies(self) -> []:
        return self.__films

    def __verify_person(self, person: Person) -> bool:
        """
        Se o nome da Pessoa for fazio retorna TRUE.
        """
        #return person.name is None
        if person.name == "":
            return True
        else:
            return False

    def __verify_film(self, filme: Filme) -> bool:
        if filme.titulo == "":
            return True
        else:
            return False

