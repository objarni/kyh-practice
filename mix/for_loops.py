print('\nMed range(0, 5):')
for i in range(0, 5):
    print(i)

print('\nMed listor:')
min_lista = ["abc", "def"]
for elem in min_lista:
    print(elem)

print('\nMed enumerate och lista:')
min_lista = ["abc", "def"]
for num, elem in enumerate(min_lista):
    print(num, elem)

print('\nMed dict:')
min_dict = {
    "Olof": True,
    "Lisa": True
}
for key in enumerate(min_dict):
    print(key)

print('\nMed dict och enumerate:')
min_dict = {
    "Olof": True,
    "Lisa": True
}
for num, key in enumerate(min_dict):
    print(num, key)
