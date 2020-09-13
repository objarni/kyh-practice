'''
9.1 Fixa så detta program fungerar igen.
9.2 Byt till f-string!
9.3 Gör så att programmet frågar efter antal uppgifter att lösa
9.4 Låt programmet fråga användaren vilket största talet ska vara
'''
import random


# Jag väljer att skicka in den data som behövs till game-funktionen
def game(number_of_questions, max_value):
    correct_answers = 0
    # range med bara ett argument ger i = 0, 1, .., n - 1
    # d.v.s lika många varv som number_of_questions
    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        answer = input(f"{a} + {b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a + b}")
            print("---")

        print(f"Du fick {correct_answers} av {number_of_questions} rätt.")


if __name__ == '__main__':
    # All data till game bestäms innan game ens startar!
    # Obs: det går självklart att ställa dessa frågor
    # inuti game() också, men jag tycker om att "balansera"
    # program så inte allt ligger i en klump. Små, fokuserade
    # block av kod = mindre risk för buggar, lättare att läsa
    # och så vidare, ni fattar. :)
    number = int(input("Hur många frågor?"))
    max_value = int(input("Största tal?"))
    game(number, max_value)
