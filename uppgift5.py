import random

max_number = 100
a_random_int = random.randint(1, max_number)
print(f"Jag tänker på ett tal mellan 1 och {max_number}. Gissa vilket!")


def mainloop():
    guess_count = 0

    while True:
        guessed_number = ask_number()
        guess_count += 1

        if guessed_number == a_random_int:
            print("Rätt!")
            break

        if guessed_number < a_random_int:
            print("Fel, mitt tal är större. Gissa igen!")

        if guessed_number > a_random_int:
            print("Fel, mitt tal är mindre. Gissa igen!")

    return guess_count


def ask_number():
    text = input("Din gissning: ")
    as_number = int(text)
    return as_number


print(f"Du behövde {mainloop()} gissningar.")
