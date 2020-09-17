'''
27.1 Det här är lite Python-kod. Spara den i data.json fil och översätt till JSON-format!
Obs! Ingen kod i JSON!

contents = [
    {
        'what': 'Energi',
        'value': 385,
        'unit': 'kcal',
        'rightalign': False
    },
    {
        'what': 'Fett',
        'value': 2.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav mättat fett',
        'value': 1.7,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Kolhydrat',
        'value': 82,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav sockerarter',
        'value': 79.5,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Fiber',
        'value': 6.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Protein',
        'value': 4.6,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Salt',
        'value': .48,
        'unit': 'g',
        'rightalign': False
    }
]

27.2 Som ni kanske sett är det en lista på ingredienser i någon produkt. Kika på nedanstående bild i en browser,  och bygg ett Pythonscript som skriver ut en liknande "tabell" på konsollen:

      https://www.oboy.se/~/media/oboy/se/images/products/original-mobile.png

Tips: Tabellens första kolumn ska vara 25 tecken bred, och andra kolumen 12.
Tips 2: Notera att det finns ett attribut "rightalign" i datan, som beskriver om "what" ska justeras till vänster eller höger!
'''

# förlaga
# https://www.oboy.se/~/media/oboy/se/images/products/original-mobile.png?la=sv-SE


contents = [
    {
        'what': 'Energi',
        'value': 385,
        'unit': 'kcal',
        'rightalign': False
    },
    {
        'what': 'Fett',
        'value': 2.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav mättat fett',
        'value': 1.7,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Kolhydrat',
        'value': 82,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'varav sockerarter',
        'value': 79.5,
        'unit': 'g',
        'rightalign': True
    },
    {
        'what': 'Fiber',
        'value': 6.7,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Protein',
        'value': 4.6,
        'unit': 'g',
        'rightalign': False
    },
    {
        'what': 'Salt',
        'value': .48,
        'unit': 'g',
        'rightalign': False
    }
]

for item in contents:
    what = item['what']
    value = item['value']
    unit = item['unit']
    per_100 = f"{value} {unit}"
    if item['rightalign']:
        print(f"{what:>25}{value:>12} {unit}")
    else:
        print(f"{what:<25}{value:>12} {unit}")
