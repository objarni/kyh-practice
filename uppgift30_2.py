'''
Träna slicing av strängar och listor!

Reg.nr på bilar i Sverge skrivs traditionellt* med tre bokstäver och tre siffror.

1. Bygg ett program som låter användaren mata in ett reg.nr och skriv ut de två grupperna
var för sig; använd slicing-syntax för att dela upp inputsträngen.

Ex.

Ange regnr: ABC663
Bokstävsgrupp: ABC
Siffergrupp: 663

2. Bygg ett program där användaren matar in ett gäng heltal med komma emellan, och skriver ut följande:
    Ange tal med komma emellan: 1,2,3,5,100
    Första talet: 1
    Sista talet: 100
    Summan av talen: 111
    Talen baklänges: 100, 5, 3, 2, 1

Tips: Använd slicing och inbyggda funktionen sum().
Tips 2: Det går att lösa "Talen baklänges" på två sätt: det lätta sättet
   är med inbyggda funktionen reverse(). Det svåra sättet är med slicing syntax!
   Pröva båda :)

'''

def run():
    indata = input("Mata in några heltal: ")
    nums_as_strings = indata.split(",")
    backwards = ', '.join(nums_as_strings[::-1])
    total = sum([int(elem) for elem in nums_as_strings])
    print(f"Första talet: {nums_as_strings[0]}")
    print(f"Sista talet: {nums_as_strings[-1]}")
    print(f"Summering: {total}")
    print(f"Talen baklänges: {backwards}")



if __name__ == '__main__':
    run()
