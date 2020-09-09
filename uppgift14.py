FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
COLORS = ['blue', 'magenta']

def run():
    # Split för att dela med kommatecken
    # string -> list of string
    basket = input("Basket: ").split(',')
    cars = []
    fruits = []
    colors = []
    rest = []
    for item in basket:
        # För att klara av mellanslag före och efter
        # komma används strip
        item = item.strip()
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in COLORS:
            colors.append(item)
        else:
            rest.append(item)
    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(colors, 'Colors')
    write_things(rest, 'Misc')


def write_things(items, kind):
    # Notera att f-string kan ha uttryck
    # som len(items) inte bara variabler!
    print(f"{kind.upper()} ({len(items)} st)")
    # .sort() sorterar listan "in-place" d.v.s
    # ändring av items sker
    # om man istället skrivit
    #     items2 = sorted(items)
    # .. så hade items inte ändrats.
    items.sort()
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()
