import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


# definition av ny klass "Djur"
class Djur:

    # init "konstruerar" en "instans" av klassen "Djur"
    # andra: konstruktor eller constructor
    # Tänk det som att ett objekt är en dictionary med fancy syntax
    # (punkt istället för brackets för att accessa innehållet)
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url



if __name__ == '__main__':

    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    skalbagge = Djur('Skalbagge', False, 'https://sv.wikipedia.org/wiki/Skalbagge')

    djur.append(zebra)
    djur.append(tiger)
    djur.append(skalbagge)

    html = '<html><table>'
    for d in djur:
        cell_2 = 'Vegetarian'
        if d.carnivore:
            cell_2 = 'Köttätare'
        html += f'<tr><td><a href="{d.wiki_url}">{d.name}</a></td><td>{cell_2}</td></tr>'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
