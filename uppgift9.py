'''
9.1 Fixa så detta program fungerar igen.
9.2 Byt till f-string!
9.3 Gör så att programmet frågar efter antal uppgifter att lösa
9.4 Låt programmet fråga användaren vilket största talet ska vara
'''
import random


def game(number_of_questions, max_value):
    correct_answers = 0
    for i in range(number_of_questions):
        a = random.randint(1, max_value)
        b = random.randint(1, max_value)
        answer = input(f"{a} + {b}")
        number = int(answer)

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

        print(f"Du fick {correct_answers} av {number_of_questions} rätt.")


if __name__ == '__main__':
    number = int(input("Hur många frågor?"))
    max_value = int(input("Största tal?"))
    game(number, max_value)
