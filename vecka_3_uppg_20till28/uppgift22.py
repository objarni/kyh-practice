'''
Telefonkatalogen igen!

Vi ska kika på hur man sparar till .json också, inte bara hur man läser.

Ta en kopia på uppgift 18 (telefonkatalogen) genom att ta en kopiera Olofs
lösning i kyh-practice!

Bygg nu ut programmet så att telefonboken:

1) laddas in vid boot ifrån "phonenumbers.json"
   (om filen inte finns, se till så programmet inte kraschar!)
2) sparas varje gång ett nytt nummer läggs till

Tips: använd p.exists() eller try .. except för (1)
Tips 2: json.dumps kommer behövas
'''
import json
from pathlib import Path


def main():
    # Försök läsa in telefonboken från filen phonebook.json
    p = Path('phonebook.json')
    try:
        content = p.read_text(encoding='utf8')
        people = json.loads(content)
    except FileNotFoundError:
        # Det gick inte; börja med en tom dicionary!
        people = {}

    # Jag lade till en while-true loop så man kan se vad man lägger
    # till i dict:en; det står inte egentligen i uppgiften om ni
    # undrar! :)
    while True:
        # f-string + len() för att skriva ut antal nummer
        print(f"Det finns {len(people)} nummer i telefonkatalogen.")

        svar = input("[S]lå upp eller [L]ägg till? ")
        svar = svar[0].upper()  # plocka ut första tecknet bara, och gör det alltid STORT
        if svar == 'S':
            vem = input("Vem vill du ringa?")
            # Slå upp namnet användaren matar in m.h.a "in" keyword (lätt att läsa!)
            if vem not in people:
                # key fanns inte i dict
                print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
            else:
                # key fanns i dict; ta reda på value m.h.a indexering som göra med raka klamrar
                # (precis som med listor fast nycklar måste inte vara heltal!)
                number = people[vem]
                print(f"Numret till {vem} är {number}")

        elif svar == 'L':
            namn = input("Ange personens förnamn: ")
            tfn = input("Ange telefonnummer: ")
            people[namn] = tfn
            # Konvertera från dictionary till sträng med dumps
            # Tips: indent ger trevlig läsbar json-fil!
            content = json.dumps(people, indent=2)
            p.write_text(content, encoding='utf8')

        else:
            print("Förstår inte, avbryter programmet.")
            # Avbryter while True och då tar main slut, d.v.s programmet avslutas
            # eftersom det inte står något mer i Pythonfilen på rad 69!
            break


if __name__ == '__main__':
    main()
