import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100. Gissa vilket!")


def mainloop():
    antal_gissningar = 0
    while True:
        as_number = ask_number()
        antal_gissningar += 1

        if as_number == n:
            print("Rätt!")
            break

        if as_number < n:
            print("Fel, mitt tal är större. Gissa igen!")

        if as_number > n:
            print("Fel, mitt tal är mindre. Gissa igen!")
    return antal_gissningar


def ask_number():
    text = input("Din gissning: ")
    as_number = int(text)
    return as_number


antal_gissningar = mainloop()

print("Du behövde " + str(antal_gissningar) + " gissningar.")
