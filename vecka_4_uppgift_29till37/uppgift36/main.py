'''
Vi ska öva lite på att dela upp program i moduler!

Skapa en mapp i erat kyh-practice som heter "uppgift36".
I den mappen, som blir vår "app", skapa två Pythonscript:

    main.py   # huvudprogrammet som ni kör
    pwstrength.py  # en hjälpmodul som main använder sig av

main.py ska fråga användaren efter ett lösenord, och anropa en funktion compute_strength(pw) [som ska bo i
pwstrength.py] som ger ut ett värde 0-3 beroende på följande regler:

  a) om lösenordet är mer än 10 tecken långt får det +1 poäng
  b) om lösenordet innehåller både siffror och bokstäver (det räcker med de engelska bokstäverna) så får det +1 poäng
  c) om lösenordet innehåller någon av symbolerna “#%&+_-” får det +1 poäng
  d) om lösenordet innehåller något annat tecken än bokstäver, siffror och symbolerna i (3) är det ogiltigt och får 0
  poäng.

Tips: Det kan behövas att ni skriver "from uppgift36.pwstrength import compute_strength" om inte "import pwstrength"
fungerar. Tänk på diskussionen kring import/paket/moduler vi hade.
'''
