import random

n = random.randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100. Gissa vilket!")
antal_gissningar = 0

while True:
    text = input("Din gissning: ")
    as_number = int(text)
    antal_gissningar += 1

    if as_number == n:
        print("Rätt!")
        break

    if as_number < n:
        print("Fel, mitt tal är större. Gissa igen!")

    if as_number > n:
        print("Fel, mitt tal är mindre. Gissa igen!")

print(f"Du behövde " + str(antal_gissningar) + " gissningar.")
