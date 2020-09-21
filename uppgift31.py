'''
Ta en kopia på lösningen av uppgift 30!

31.1 I nya filen, byt ut for-loopar mot list-comprehensions så mycket ni kan.
     Jämför de två filerna, vilken tycker ni är mest läsbar/enklast att förstå?

31.2 Utöka 30.2 med följande utskrifter:

    Udda tal: 1, 3, 5
    Jämna tal: 2, 100

Tips: det går att skriva if-uttryck i list-comprehensions! Googla och härma!
'''


def run():
    indata = input("Mata in några heltal: ")
    nums_as_strings = indata.split(",")
    backwards = ', '.join(nums_as_strings[::-1])
    nums_as_ints = [int(elem) for elem in nums_as_strings]
    total = sum(nums_as_ints)
    odds = [i for i in nums_as_ints if i % 2 == 1]
    evens = [i for i in nums_as_ints if i % 2 == 0]
    print(f"Första talet: {nums_as_strings[0]}")
    print(f"Sista talet: {nums_as_strings[-1]}")
    print(f"Summering: {total}")
    print(f"Talen baklänges: {backwards}")
    print(f"Udda tal: {pretty_intlist(odds)}")
    print(f"Jämna tal: {pretty_intlist(evens)}")


def pretty_intlist(list_of_ints):
    return ', '.join([str(elem) for elem in list_of_ints])


if __name__ == '__main__':
    run()
