name = "Kala Pál" # string
age = 32          # int
weight = 75.4     # float (nem egész szám) - lebegőpontos szám
married = True    # bool
weight -= 0.4
print(f"""Szia! {name} vagyok, {age} éves.
A testúlyom {weight} kg.
Házas vagyok: {married}""")

print("Hello")

myFloat = 10
print(myFloat)       # 10
print(type(myFloat)) # <class 'int'>

myFloat = 10.0
print(myFloat)       # 10.0
print(type(myFloat)) # <class 'float'>

# Operátorok (+, -, *, /, stb.)

# 1. Aritmetikai operátorok (+, -, stb.)
print(2 + 3)    # 5
print(5 - 3)    # 2
print(4 * 3)    # 12
print(9 / 3)    # 3.0   (osztás eredménye mindig float lesz)
print(4 / 3)    # 1.33333333333333
print(int(9/3)) # 3
print(9 // 3)   # 3     (maradék nélküli osztás) (mindig int lesz az eredmény)
print(4 // 3)   # 1
print(11 % 3)   # 2   11-ben a 3 megvan 3 szor, maradék a 2 (maradékos osztás)
print(2 ** 8)   # 2^8 = 256   hatványozás
print(25 ** (1/2)) # 25^0.5 = gyök(25) = 5

# 2. Értékadó operátorok ( = )
alma = 5
print(alma)   # 5
alma += 3  
print(alma)   # 8
alma -= 4
print(alma)   # 4
alma *= 3
print(alma)   # 12
alma /= 2
alma = int(alma)
print(alma)   # 6
alma //= 5
print(alma)   # 1
alma **= 12
print(alma)   # 1

# 3. Összehasonlító operátorok (relációs jelek)
# Eredménye mindig bool típusú
print(4 == 7) # False
print(1 == 1) # True
print(4 != 7) # True  (Nem egyenlő)
print(1 != 1) # False
print(3 > 3)
print(3 >= 3)
print(2 < 5)
print(5 <= 8)

# 4. Logikai operátorok (és, vagy, nem)
print(True and False) # False
print(True or False)  # True
print(not True)       # False

# 5. Egyéb operátorok (in)
# in operátor megnézi, hogy a bal oldali érték benne van-e a jobb oldali értékben
print("a" in "almafa") # True
print("c" in "almafa") # False


# Feladat: adott egy szám, döntsük el, hogy poz, neg vagy pedig 0

a = 0
if a > 0:
    print("pozitív")
elif a < 0:
    print("negatív")
else:
    print("nulla")




