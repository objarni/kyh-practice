# Importera den inbyggda modulen "random", d.v.s gör randint m.fl
# tillgängliga i detta script
import random

# Ta fram ett heltal ur 1, 2, 3, ... , 20 slumpmässigt
n = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20. Guess which?")

# Loopa för evigt... alltså tills "break" nås  :)
while True:

    # Ta in sträng från användaren
    text = input("Your guess: ")

    # (Försök) Konvertera sträng till heltal
    # str -> int
    as_number = int(text)

    # Är användarens tal det datorn "tänker" på?
    if as_number == n:
        print("Correct!")
        # break bryter ur while-loopen, vilket avslutar programmet
        # eftersom det inte finns någon mer kod nedanför while-loopen
        break

    # Ej lika med, så större eller mindre än.
    if as_number < n:
        print("Wrong, my number is higher... Try again!")
    if as_number > n:
        print("Wrong, my number is lower... Try again!")
