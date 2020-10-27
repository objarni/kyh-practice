
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]

def age_sorter(person):
    return person[2]

on_surname = sorted(people, key=age_sorter)

for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

