"""
Repetition och träning på funktioner!

1. Skriv en funktion som beräknar maximum (=största värdet) av tre tal (utan att använda max()!)
2. Skriv en funktion som summerar alla tal i en lista. Inbyggda funktionen sum() ska ej användas
3. Skriv en funktion som räknar ut produkten (=multiplikation av alla tal) av en lista av heltal
"""


def maximum(a, b, c):
    if a < b > c:
        return b
    if b < a > c:
        return a
    if a < c > b:
        return c
    return a


def summa(ls):
    s = 0
    for elem in ls:
        s += elem
    return s

def produkt(ls):
    p = 1
    for elem in ls:
        p *= elem
    return p
