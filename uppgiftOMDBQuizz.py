'''
'''

import json
import random
from pathlib import Path

import requests
from pprint import pprint

# algo: ta random letter, random 10. visa
# 1) årtal, skådespelare (10p)
# 2) awards, runtime
MOVIELIST = Path('uppgift27.txt').read_text(encoding='utf8').splitlines()


def main():
    for i in range(1):
        movie = get_random_movie()
        title = movie['Title']
        print(title)
        if title.startswith('The '):
            title = title[4:]
        print(title)
        print("Vilken film tänkar jag på?")
        print(f"Första bokstaven är {title[0]}.")
        print(f"Filmen kom ut {movie['Year']}.")
        print(f"Skådisar: {movie['Actors']}")
        print(f"Den regisserades av {movie['Director']}.")
        guess = input("Vad heter filmen? ")
        if guess.lower() == title.lower():
            print("Rätt!")
        else:
            print(f"Fel! Jag tänkte på {title}")


def get_random_movie():
    movie = random.choice(MOVIELIST)
    r = requests.get("http://www.omdbapi.com/", params={"t": movie, "apikey": "9f6d550c"})
    text = r.text
    result = json.loads(text)

    return result


main()
