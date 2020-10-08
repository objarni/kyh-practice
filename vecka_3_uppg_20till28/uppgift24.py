'''
Nu ska vi använda oss av kunskapen kring JSON och att installera paket från PyPI (cheese shop) på riktigt!

Börja med att utöka "requirements.txt" med paketet "requests":

    pygame
    requests

.. och låt PyCharm installera det nya paketet när frågan dyker upp.

1. Pröva att ladda ned denna URL i browsern:

   https://proagile.se/api/publicEvents

2. Läs på hur man gör en GET med requests-API:et. Skriv ut r.text med print mha ett Pythonprogram
    r = requests.get( ... )  # fixa rätt parametrar! r.text är råa strängen som är resultatet

3. Använd nu istället pprint för att skriva ut r.json()

4. Leta upp alla "startDate" i datan, och skriv ut dem.

'''
import json
import requests

r = requests.get("https://proagile.se/api/publicEvents")

text = r.text
list = json.loads(text)
# alternativt: list = r.json()

for element in list:
    print(element['startDate'])
