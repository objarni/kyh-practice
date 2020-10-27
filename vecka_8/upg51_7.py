
class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


anna = Person("Anna", "Persson", 42)
lova = Person("Lova", "Andersson", 35)
alex = Person("Alex", "Börjesson", 10)
people = [anna, lova, alex]

# def age_sorter(person):
#     return person.age

on_surname = sorted(people, key=lambda p:p.last)

for person in on_surname:
    print(f"{person.first} {person.last} ({person.age} år)")

