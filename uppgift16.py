# Vi behöver bara Path från pathlib
from pathlib import Path

def run():
    # Gå igenom "system.log" filen rad för rad
    # genom att splitta content vi får ifrån read_text
    # på radslut
    for line in Path('system.log').read_text().splitlines():
        # Så fort vi får syn på BEAR eller X-RAY
        # printa loggraden!
        if 'BEAR' in line or 'X-RAY' in line:
            print(line)

if __name__ == '__main__':
    run()
