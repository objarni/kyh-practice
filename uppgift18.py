'''
18.1 Förklara vad nedanstående program gör för varandra!

people = {
    "Fredrik": "0702778511",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789"
}

vem = input("Vem vill du ringa?")
if vem not in people:
    print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
else:
    number = people[vem]
    print(f"Numret till {vem} är {number}")

18.2 Modifiera programmet så antalet personer i telefonkatalogen skrivs ut när man kör programmet
18.3 Flytta in all kod i en "main"-funktion som anropas på slutet av programmet. Main ska varken ta argument, eller returnera något
18.4 Ge användaren ett val mellan "Slå upp" och "Lägg till/skriv över" nummer.
'''


def main():
    # Vår telefonkatalog är "hårdkodad" i programmet, och representeras
    # av en dictionary (dict).
    people = {
        "Fredrik": "0702778511",
        "Olof": "123456789",
        "Lisa": "9999999999",
        "Bodil": "555-666-789"
    }

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

        else:
            print("Förstår inte, avbryter programmet.")
            # Avbryter while True och då tar main slut, d.v.s programmet avslutas
            # eftersom det inte står något mer i Pythonfilen på rad 69!
            break


if __name__ == '__main__':
    main()
