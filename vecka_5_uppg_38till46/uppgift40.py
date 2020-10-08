"""
1. Skriv en funktion som "vänder" en textsträng baklänges - utan att använda "reverse" (eller [::-1])!
Använd istället strängar eller listor, och en for-loop.
T.ex. "12345" blir "54321".

2. Skriv en funktion som tar in en textsträng, och returnerar antalet stora bokstäver i strängen.

3. Skriv en funktion som avgör om ett tal ligger mellan två andra tal.
t.ex.
  inrange(value=1, min=2, max=3) blir False eftersom 1 ligger utan för 2 till 3.
  inrange(value=10, min=0, max=100) blir True eftersom 10 ligger mellan 0 och 100.
"""


def backwards(s):
    result = []
    for i in range(len(s)):
        result.append(s[-i - 1])
    return ''.join(result)


def count_capital(s):
    return sum(char.isupper() for char in s)


def inrange(min, value, max):
    return min <= value <= max
