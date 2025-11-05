# 1. feladat:
szamok = [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

# 2. feladat:
összeg = 0
for i in range(len(szamok)):
    if szamok[i] != -1:
        összeg += szamok[i]

print("\n2. feladat")
print(f"Összesen {összeg} kerékpárost számoltak.")

# 3. feladat: [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]
print("\n3. feladat")
print("Óránkénti mérések:")
összeg6 = 0
összeg7 = 0
összeg8 = 0
összeg9 = 0
for i in range(0, 4):
    if szamok[i] != -1:
        összeg6 += szamok[i]
    if szamok[i+4] != -1:
        összeg7 += szamok[i+4]
    if szamok[i+8] != -1:
        összeg8 += szamok[i+8]
    if szamok[i+12] != -1:
        összeg9 += szamok[i+12]

print(f"6 órától {összeg6} kerékpáros")
print(f"7 órától {összeg7} kerékpáros")
print(f"8 órától {összeg8} kerékpáros")
print(f"9 órától {összeg9} kerékpáros")

# 4. feladat: [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

max_index = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[max_index]:
        max_index = i
# index 0 -> 6:15      6 óra * 60 + 15 = 375 perc
# index 1 -> 6:30   # 390
# ...
# index 9 -> 8:30   # 510
# időpont(i) = 375 + i * 15

# 510 // 60 = 8
# 510 % 60 = 30

időpont = 375 + max_index * 15
print("\n4. feladat")
print(f"Az áthaladók maximális száma: {szamok[max_index]}; a rögzités időpontja: {időpont // 60}:{időpont % 60}")