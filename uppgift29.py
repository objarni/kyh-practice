'''
Bygg ett Pythonprogram som genererar en random life quote med random getbild!

Hur? Jo genom att utgå ifrån bifogad fil, och byta ut "QUOTE_TEXT" mot get-citat som ni hittar i följande API:
   https://api.adviceslip.com/advice

Gör bara ett GET-request mot det så får ni random life advice!

HTML-fil att utgå ifrån bifogas som "uppgift29_template".html. Spara den i er kyh-practice.

Programmet ska alltså skapa en ny fil "goat_quote.html" där QUOTE_TEXT ersatts av ett nytt quote, och starta "goat_quote.html" i webbläsaren.

Tips: ni kommer behöva använda requests, webbrowser, och inbyggda replace() funktionen i string. Diskutera gärna igenom allt ni behöver göra först!
'''

import webbrowser
from pathlib import Path
from pprint import pprint

import requests


def random_life_advice():
    r = requests.get("https://api.adviceslip.com/advice")
    pprint(r.json())
    return r.json()['slip']['advice']


def generate_random_quote_to(p):
    quote = random_life_advice()
    html = Path("uppgift29_template.html").read_text(encoding='utf8')
    html = html.replace('QUOTE_TEXT', quote)
    p.write_text(html, encoding='utf8')


if __name__ == '__main__':
    p = Path("uppgift29.html")
    generate_random_quote_to(p)
    webbrowser.open(str(p))
