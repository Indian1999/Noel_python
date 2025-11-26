import math
import random

tort_szam = 3.14
egesz_szam = 9
string = "Kiscica"
logikai_ertek = True or False

print("Kiírok valami szöveget.")
print("A string változó ezt a szöveget tárolja: " + string)
#print("Az egesz_szam értéke: " + egesz_szam) # TypeError: can only concatenate str (not "int") to str
print("Az egesz_szam értéke:", egesz_szam) # vesszővel van elválasztva -> a print fgv. 2 paramétert kap
# A print függvény a paraméterek szóközzel választja el
print("Az egesz_szam értéke: " + str(egesz_szam))
print("Az egesz_szam értéke: ", egesz_szam, sep=" Kiscica ")
print(1,2,3,4,5,6,7,7,8,9,9,43,2, sep=", ", end = "")
print("valami") # 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 43, 2valami
print(logikai_ertek, end="\n" + "#" * 50 + "\n")
print("valami")

print("""Ez itt egy
Több sorból álló string amit ki fogok
iratni a print függvénnyel.
      Fontos hogy figyeljünk arra, hogy hol
kezdődik a sor, mert ha egy sort bentebb kezdek,
akkor a kiiratásnál is bentebb fogja kezdeni...""")
print("valamit")

valasz = "20"#input("adj meg valamit: ")
print(valasz)
print(type(valasz)) # Mindig string az input eredménye
print(int(valasz) * 2)

# Feladat: Cseréljük meg két változó értékét:
a = 10
b = 20
print(f"a = {a}, b = {b}")
# Alap módszer (minden prog nyelven műküdik)
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")
# Python specifikus megoldás:
a, b = b, a
print(f"a = {a}, b = {b}")

# 1. feladat: Olvassuk be egy kör átmérőjét, és ez alapján írjuk ki a területét
# T = r^2 * pi
# d = r * 2
d = 5#float(input("Add meg a kör átmérőjét: "))
r = d / 2
terület = r ** 2 * 3.14
print(f"A kör területe: {terület} (pi = 3.14)")
terület = r ** 2 * math.pi
print(f"A kör területe: {terület} (pi = math.pi)")

# List comprehension
lista = [5, 8, 9, 13, 2]
print(lista) # [5, 8, 9, 13, 2]
lista = [6 for i in range(10)] 
print(lista) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
lista = [i for i in range(1, 10, 2)]
print(lista) # [1, 3, 5, 7, 9]
lista = [i**2 for i in range(-5, 6)]
print(lista) # [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]

# 2. feladat: Rendezzünk egy listát növekvő sorrendbe
random.seed(42)
lista = [random.randint(-20, 100) for i in range(30)] # 30 db -20 és 100 közötti véletlen egész számot
print(lista)
# Egyszerű cserés rendezés
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(f"Rendezve: {lista}")

# 3. feladat: Adott egy lista, gondoskodjunk róla, hogy minden eleme 7-tel osztható legyen
# ha nem osztható egy elem héttel -> növeljük addig, amíg 7-tel osztható nem lesz
# pl.: [13, 7, 3, 25, 12] -> [14, 7, 7, 28, 14]

for i in range(len(lista)):
    while lista[i] % 7 != 0:
        lista[i] += 1

print(lista)


# 4. feladat:
# Írjunk ki minden sorba annyi #-t amennyi a lista[i]. elemének az értéke
# lista[i] < 0 -> 0 # -t írunk ki

for i in range(len(lista)):
    if lista[i] > 0:
        print("#" * lista[i])

# 5. feladat: Számoljuk meg, hogy melyik számból van a legtöbb a listában?
lista[0] = -21
print(lista)
max_index = None
max_value = -float("inf")
for i in range(len(lista)):
    szamlalo = 0
    for j in range(len(lista)):
        if lista[i] == lista[j]:
            szamlalo += 1
    if szamlalo > max_value:
        max_value = szamlalo
        max_index = i

print(f"A legtöbbszőr előforduló szám a {lista[max_index]}, a {max_index}. indexen található az első előfordulása. {max_value} db van összesen a listában.")

# 6. feladat: Írjuk ki, hogy hány páros, hány páratlan szám van a listában
# 0 jelen esetben se nem páratlan se nem páros, számoljuk meg azt is, hogy hány 0 van
even_counter = 0
odd_counter = 0
zero_counter = 0
for i in range(len(lista)):
    if lista[i] < 0:
        continue # Ha negatív, akkor ugorják át ezt a számot
    if lista[i] == 0:
        zero_counter += 1
    elif lista[i] % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1

print(f"Páros számok: {even_counter}") 
print(f"Páratlan számok: {odd_counter}") 
print(f"0-k száma: {zero_counter}") 


