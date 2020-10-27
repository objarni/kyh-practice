'''
51.1 Skriv om funktionen add_as_def som lambda, och lagra i en variabel

def add_as_def(a, b):
    return a + b

# add_as_lambda = ???


51.2 Skriv om obj som en funktion "upper"

obj = lambda s: s.upper()


51.3 Översätt denna lambda till en vanlig def funktion

join_as_lambda = lambda strings, inbetween: inbetween.join(strings)


51.4 Vad kommer följande program att skriva ut? Läs och diskutera först.
Testkör därefter, och förklara varför ni får det resultat ni får...

anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[1])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")


51.5 Skriv ett program som utgår ifrån ovanstående, men skriver ut personerna i åldersordning.

51.6 Utgående ifrån förra programmet, ändra så att en "def age_sorter" funktion används istället för lambdan,
med hjälp syntaxen key=age_sorter. Vilket sätt tycker ni är tydligast?

51.7 Skriv om föregående program så att det använder sig av en class Person med attributen first, last och age
istället för tuppler. Vilken form tycker ni är lättast att läsa?

51.8 Varför kan inte hello skrivas som lambdauttryck? Försök gärna skriva om det till lambdaform!

def hello(name):
    import random
    rnd_age = random.randint(1, 150)
    print(f"Hello {name}! I guess your age is {rnd_age}")
'''

