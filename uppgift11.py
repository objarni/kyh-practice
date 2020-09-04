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

        while True:
            answer = input(f"{a} + {b}")
            try:
                number = int(answer)
                break
            except ValueError:
                print("Inte ett heltal! Försök igen.")

        if number == a + b:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f"Fel... Det blir {a+b}")
            print("---")

        print(f"Du fick {correct_answers} av {number_of_questions} rätt.")




if __name__ == '__main__':
    try:
        number = int(input("Hur många frågor?"))
    except ValueError:
        print("Inte ett heltal! Väljer 3 frågor")
        number = 3
    try:
        max_value = int(input("Största tal?"))
    except ValueError:
        print("Inte ett heltal! Väljer max = 10")
        max_value = 10

    game(number, max_value)
