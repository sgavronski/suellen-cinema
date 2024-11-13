from person import Person


class Database:

    __people = [] #criação de lista chamada __people

    def add_person(self, person: Person):
        self.__people.append(person)
        #adiciona(append) à lista __people o dado da pessoa (person)

    def get_person(self, index: int) -> Person:
        return self.__people[index]
    #self= database; retorna a pessoa que está na lista __people correspondente ao numero (index) pedido

    def get_all_person(self) -> []:
        return self.__people
    #retorna todas as pessoas que estão na lista __people

    #pergunta 1 = por que "self"? Todos os selfs aqui referem-se à Database || SELF É O NOME DA CLASSE!
    #pergunta 2 = não entendi o parâmetro person:person na função add_person
    #pergunta 3 = get all person chama o database. Não entendi o "-> []"
