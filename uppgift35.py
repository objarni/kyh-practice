import os
from pprint import pprint

print(os.getcwd())
from qs import QuizzWebServiceAPI


def run():
    api = QuizzWebServiceAPI()
    for n, q in enumerate(api.get_all_questions()):
        print(f"Fråga {n + 1}: {q['prompt']}")
        # pprint(q)
    while True:
        questions = len(api.get_all_questions())
        answer = menu(questions)
        if answer == "1":
            question = input("Ange ny fråga: ")
            right = input("Ange rätt svar: ")
            alternatives = [alt.strip() for alt in input("Skriv några felaktiga svar med komma emellan: ").split(',')]
            api.add_question(prompt=question, answer=right, alternatives=alternatives)


def menu(questions):
    print(f"""Det finns {questions} frågor i quizz-db. Gör ett val:
   1. Lägg till fråga
   2. Avsluta programmet""")
    answer = input(" # ")
    return answer


if __name__ == '__main__':
    run()
