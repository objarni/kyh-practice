# Vi behöver bara denna modul ifrån Pythons standardbibliotek
import random


def gibberish():
    # Här är det sätt jag tänkte mig att ni skulle göra
    # med de kunskaper ni hade vid tillfället
    saker = ["En app","Ett bananskal","En labyrint"]
    sak = saker[random.randint(0, len(saker)-1)]

    # Här är ett annat sätt som någon upptäckte m.h.a
    # google :)
    kan_uttryck = random.choice(
        ["laddas ner till mobiltelefonen",
         "slängas i en papperskorg",
         "underhålla barnen"
        ])
    grupp = random.choice(["finländare", "skåningar", "göteborgare"])
    smitta = random.choice(["coronaviruset", "kärleksbaciller", "avundsjuka"])
    person = random.choice(["Winston Churchill", "Adolf Hitler"])
    yrkesroll = random.choice(["generaldirektör", "städare"])

    # Använder multiline string literal för läsbarhetens skull
    return f"""
{sak} som kan {kan_uttryck} ska varna
{grupp} som kommit nära någon som smittats med {smitta}.
- Jag tycker ni i Sverige borde överväga att göra något
liknande, säger {person}, {yrkesroll} för
Finska institutet för hälsa och välfärd, THL."""

if __name__ == '__main__':
    # Jag valde att bygga en funktion som producerar
    # slumptexten
    text = gibberish()

    # Skriv ut texten på skärmen
    print(text)
