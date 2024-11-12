from person import Person


class Database:

    __people = []

    def add_person(self, person: Person):
        self.__people.append(person)

    def get_person(self, index: int) -> Person:
        return self.__people[index]

    def get_all_person(self) -> []:
        return self.__people
