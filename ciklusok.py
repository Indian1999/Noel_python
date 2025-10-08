# Ciklus (for, while)

# Számlálós ciklus (for)

"""
for i in range(5): # [0, 1, 2, 3, 4] 
    print(i, end=" kiscica ") 
print()
print("Szia")
print("Hello")

for i in range(2, 6): # [2, 3, 4, 5]
    print(i, end=" ") 
print()

for i in range(20, 10, -1): # [20, 19, 18, ..., 12, 11]
    print(i, end=" ") 
print()

for i in range(5, 51, 5): # [5, 10, 15, ..., 45, 50]
    print(i, end=" ") 
print()

# Feladat: Kérjünk be egy számot, és nézzük meg, hogy prím-e!

num = int(input("Adj meg egy poz. egész számot!\n"))
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
if isPrime:
    print("Ez egy prímszám!")
else:
    print("Nem prím!")

lista = ["kutya", "szalámi", 56, True, 3.14, "cica"]

for item in lista: # kutya, szalámi, 56, True, 3.13, cica
    print(item)

# Elől tesztelős ciklus (while)

szövegek = []
while True:
    szöveg = input("Írj valamit: ")
    if szöveg == "quit":
        break # kilép ciklusból
    else:
        szövegek.append(szöveg)

print(szövegek)
"""

num = 0
while num < 11:
    num += 1
    if num % 2 == 0:
        continue    # Következő ciklus iterációra lépünk
    print(num)





# Programozási tételek:
lista = [3, 2, 13, 29,3,2,12,-5,-9, 12, 34,-19, 0, 2, 12, 39, -9, 13, 15, 23]

for i in range(len(lista)):
    print(lista[i], end= " ")
print()

for item in lista: # item = 3, 2, 29, 3, 2, 12, ...
    print(item, end = " ")
print()

# Határozzuk meg a lista elemeinek az összegét!

összeg = 0
for item in lista:
    összeg += item

# Mennyi a lista elemeinek az átlaga?

# Melyik a legnagyobb/legkisebb szám a listában?

# Hány negatív szám van a listában?

# Van-e a listában 13-mal osztható szám? 

oszthato13mal = False
for item in lista:
    if item % 13 == 0:
        oszthato13mal = True
        break
print("Van 13-mal osztható:", oszthato13mal)


# Feladat: Szedjük szét a listában található elemeket poz és negatív értékekre

pozLista = []
negLista = []
for item in lista:
    if item < 0:
        negLista.append(item)
    elif item > 0:
        pozLista.append(item)

print(pozLista)
print(negLista)

# Feladat: Határozzuk meg a listában a páratlan számok összegét (Feltételes összegzés)
összeg = 0
for item in lista:
    if item % 2 == 1:
        összeg += item

print("A páratlan számok összege:", összeg)

poz_összeg = 0
for item in pozLista:
    poz_összeg += item

print("A pozitív számok összeg:", poz_összeg)