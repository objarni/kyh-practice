'''
Skriv ett Pythonprogram som tar in en sträng från användaren, och skriver ut följande:

32.1 Längden på strängen
32.2 Om strängen är ett "palindrom" eller ej. Exempel på palindrom: rattar, Ebbe. Observera att programmet ska klara att användaren blandar stora och små bokstäver!
32.3 Utöka programmet så att även uttryck som "Aja Baja" anses vara palindrom, d.v.s filtrera bort alla mellanslag ifrån inputsträngen!

Tips: använd det vi lärde oss igår kring att vända en sträng och/eller lista baklänges, och join-funktionen. Även list comprehension kan komma till användning.
'''

text = input("Skriv något: ")
print(f"Texten är {len(text)} tecken lång.")

# Alternativ 1 - med replace
lowercase = text.lower().replace(' ', '')

# Alternativ 2 - med list comprehension.
lowercase = ''.join([c for c in text.lower() if c != ' '])

# Reverse m.h.a slicing! :)
lowercase_rev = lowercase[::-1]

if lowercase == lowercase_rev:
    print(f"{text} är ett palindrom!")
else:
    print(f"{text} är INTE ett palindrom!")
