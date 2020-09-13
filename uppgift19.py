'''
Spara följande i "data.json":

[
  12,
  3.5,
  4,
  true,
  false,
  "vi kan ha text också",
  "1234908",
  "99999999",
  {
    "fredrik": {
      "tfn": "12345677",
      "adress": "Banangränd",
      "email": "freddan@proagile.se"
    }
  }
]

Uppgift:
Läs in "data.json" i Python, spara i en variabel "data = json.loads(content)" i Python.
Med hjälp av debuggern, undersök datatyper ni kan hitta inuti data-variabeln.
Posta alla datatyper ni hittar som kommentarer i denna uppgift!
'''
import json
from pathlib import Path

if __name__ == '__main__':
    raw_string = Path("data.json").read_text(encoding='utf8')
    json_object = json.loads(raw_string)
    # jag sätter breakpoint på rad 35 så jag kan undersöka
    # vilka typer som finns i variablen json_object lätt
    pass
    # jag hittar följande typer:
    #  - list
    #  - int
    #  - float
    #  - bool
    #  - str
    #  - dict
