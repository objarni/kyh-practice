import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template.html')


# definition av ny klass "Djur"
class Djur:

    # init "konstruerar" en "instans" av klassen "Djur"
    # andra: konstruktor eller constructor
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    # 34.2
    def carnivore_or_vegetarian(self):
        return 'Köttätare' if self.carnivore else 'Vegetarian'

    def get_html_table_row(self):
        return f'''
<tr>
   <td>
     <a href="{self.wiki_url}">{self.name}</a>
   </td>
   <td>
     {self.carnivore_or_vegetarian()}
   </td>
</tr>
'''

if __name__ == '__main__':

    djur = []
    # Skapa två instanser av klassen "Djur"
    # instans kallas också "objekt" eller "klassinstans"
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')

    # 34.1
    skalbagge = Djur('Skalbagge', False, 'https://sv.wikipedia.org/wiki/Skalbagge')

    djur.append(zebra)
    djur.append(tiger)
    djur.append(skalbagge)

    html = '<html><table>'
    for d in djur:
        html += d.get_html_table_row()
        # 34.2
#         cell_2 = d.carnivore_or_vegetarian()
#         html += f'''
# <tr>
#    <td>
#      <a href="{d.wiki_url}">{d.name}</a>
#    </td>
#    <td>
#      {cell_2}
#    </td>
# </tr>
# '''
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
