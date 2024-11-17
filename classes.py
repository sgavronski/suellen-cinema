import person
from person import Person

def start():
    #person3 = person.Person('Suellen','Gavronski',32,'Female',1.76,66,'Python')
    person3 = Person()
    person3.name = "Suellen"
    person3.last_name = "Gavronski"
    person3.age = 32
    person3.gender = "Female"
    person3.height = 1.76
    person3.weight = 70
    person3.language = "Python"
    print(person3.print_full_name())
    print(f"The perfect {person3.name}'weight is {person3.get_ideal_weight()}")
    return person3
