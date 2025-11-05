# 1. feladat:
üvegek = [5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3]

# 2. feladat:
print("2. feladat")
lekvár = float(input("Mari néni lekvárja (dl): "))

# 3. feladat:
max_index = 0
for i in range(1, len(üvegek)):
    if üvegek[i] > üvegek[max_index]:
        max_index = i

print("3. feladat")
print(f"A legnagyobb üveg: {üvegek[max_index]} dl és {max_index + 1}. a sorban.")

# 4. feladat:
összeg = 0
for i in range(len(üvegek)):
    összeg += üvegek[i]

if összeg >= lekvár:
    print("Elegendő üveg volt.")
else:
    print("Maradt lekvár!")