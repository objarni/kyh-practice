'''
10. Skriv program som skriver ut:
1) heltalen fr.o.m. 1 t.o.m. 10 i ökande ordning
2) udda tal fr.o.m. 1 t.o.m. 49 i ökande ordning
3) heltal fr.o.m. 10 t.o.m. 1 i minskande ordning
4) summan av talen 7 t.o.m 1000
5) produkten av talen 1 t.o.m 1000
'''

print('uppgift 1')
for i in range(1, 11):
    print(i)

print('uppgift 2')
for i in range(1, 50, 2):
    print(i)

print('uppgift 3')
for i in range(10, 0, -1):
    print(i)

print('uppgift 4')
total = 0
for i in range(7, 1001):
    total = total + i
print(total)

print('uppgift 5')
product = 1
for i in range(1, 1001):
    product *= i
print(product)