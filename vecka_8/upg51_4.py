
anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[1])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

