'''
En repetitionsuppgift på JSON!

21.1 Vi har tillgång till en fil massadata.json. Ladda ner och undersök hur filen ser ut med PyCharm.

21.2 Bygg ett Pythonprogram som summerar alla värden på "total" i filen, och skriver ut på skärmen.

Tips:
 - läs på om den inbyggda funktionen "sum"
 - repetera hur man läser in en .json fil och läser ut data ifrån den
'''
import json
from pathlib import Path


def compute_total(json_object):
    entries_list = json_object['entries']
    totals = []
    for entry in entries_list:
        totals.append(entry['total'])
    return sum(totals)


def main():
    p = Path('massadata.json')
    content = p.read_text(encoding='utf8')
    json_object = json.loads(content)
    total = compute_total(json_object)
    print(f"Total = {total}")


if __name__ == '__main__':
    main()
