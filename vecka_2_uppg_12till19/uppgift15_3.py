# 15.3 Göteborgsvarvet, vilken placering kom XYZ på? Implementera resten av detta program:
#     runners_in_order = “Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus”.split()
#     vem = input(“Ange löpare du söker placering för”)



runners_in_order = "Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus".split()
vem = input("Ange löpare du söker placering för: ")
if vem in runners_in_order:
    # Obs! Listor börjar på index 0, men placeringar i Göteborgsvarvet
    # på 1! Fixa med +1 ....
    pos = runners_in_order.index(vem) + 1
    print(f"{vem} slira in på position {pos}!")
else:
    print(f"Vem är {vem}? Hitta ingen sån i listan: ")
    # Trick för att skriva ut List[str]: använd join!
    print('\n'.join(runners_in_order))
