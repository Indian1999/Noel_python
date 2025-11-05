# 1. feladat: Váltsunk át x kg-ot g-ra
kilogramm = 32.1
print(f"{kilogramm} kg = {kilogramm*1000} g")

# 2. feladat: Ugyan ez visszafelé g -> kg
g = 65387
print(f"{g} g = {g/1000} kg")

# Fahrenheit = 1.8 * °C + 32
# Celsius = (°F - 32) / 1.8
# 3. feladat: Váltsunk át x Celsius-t Fahrenheit-be
f = 78
# 4. feladat: Ugyan ez visszafelé

# 1 km = 0.62137 mi (mérföld)
# 5. feladat: Mérföld -> Km

# 6. feladat: Km -> Mérföld

# 7. feladat: Nézzük a számokat 1-től 75-ig
# Ha a szám osztható 3-mal, akkor írjuk hogy bim
# Ha egy számban szerepel a 3-as számjegy írjuk ki, hogy bam
# Ha mindkettő teljesül: bimbam

for i in range(1, 76):
    if i % 3 == 0 and "3" in str(i):
        print(i,"bimbam")
    elif i % 3 == 0:
        print(i,"bim")
    elif "3" in str(i):
        print(i, "bam")

# 8. feladat: Ellenőrizzük, hogy egy adott jelszó elég erős-e!
# A hossza 6 és 18 karakter között van
# Van benne kis és nagybetű is
# Van benne szám
# Van benne speciális karakter
password = "KetrecHarc2025!"
correct_length = len(password) >= 6 and len(password) <= 18
has_lower_case = False
has_upper_case = False
has_digit = False
has_special = False
specials = ",.-<>#&@{}<;>*~ˇ^˘°˛`˙´'+!%/=()_:?\"€$÷×\\"
print(specials)

for char in password:
    if char.islower():
        has_lower_case = True
    if char.isupper():
        has_upper_case = True
    if char.isdigit():
        has_digit = True
    if char in specials:
        has_special = True

if has_upper_case and has_lower_case and has_digit and has_special and correct_length:
    print("Megfelelő jelszó!")
else:
    print("Gyenge jelszó!")

# 9. feladat: Egy futóversenyen ezek az időpontok születtek:
nevek = ["András", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc", "Gábor", "Hugó"]
eredmények = [42.2, 38.9, 39.3, 40.2, 41.1, 42.7, 41.0, 41.7]

print(type(41))   # <class 'int'>
print(type(41.0)) # <class 'float'>

# 9.a: Mennyi idő alatt teljesítette a távot Elemér?
elemér_index = None
for i in range(len(nevek)):
    if nevek[i] == "Elemér":
        elemér_index = i

if elemér_index != None:
    print(f"{nevek[elemér_index]} {eredmények[elemér_index]} mp alatt teljesítetet a távot.")
else:
    print("Nincs ilyen nevű versenyző")

# 9.b: Ki nyerte a versenyt?
min_index = 0 # Az elején azt feltételezem, hogy a 0. szám a legkisebb
for i in range(1, len(eredmények)): # i = 1, 2, 3, 4, 5, 6, 7
    if eredmények[i] < eredmények[min_index]:
        min_index = i

print(f"A versenyt {nevek[min_index]} nyerte, {eredmények[min_index]} mp alatt teljesítette a távot.")

# 9.c: Ki futott be utoljára?
max_index = 0
for i in range(1, len(eredmények)):
    if eredmények[i] > eredmények[max_index]:
        max_index = i

print(f"Utolsónak {nevek[max_index]} végzett, {eredmények[max_index]} mp alatt teljesítette a távot.")

# 9.d: Írjuk ki azoknak a nevét és idejét, akik az átlagtól gyorsabban teljesítették a távot
osszeg = 0
for item in eredmények:
    osszeg += item
atlag = osszeg / len(eredmények)
print("Az időeredmények átlaga:", round(atlag, 2))
print("Az emberek akik az átlagtól gyorsabbak voltak:")
for i in range(len(eredmények)):
    if eredmények[i] < atlag:
        print(nevek[i], eredmények[i], "mp")


# 9.e: Írjuk ki az első három helyezett nevét (és hogy hanyadik lett)!
eredmények_copy = eredmények[:]

elso_index = 0
for i in range(1, len(eredmények_copy)):
    if eredmények_copy[i] < eredmények_copy[elso_index]:
        elso_index = i
eredmények_copy[elso_index] = float("inf") # végtelenre állítom

masodik_index = 0
for i in range(1, len(eredmények_copy)):
    if eredmények_copy[i] < eredmények_copy[masodik_index]:
        masodik_index = i
eredmények_copy[masodik_index] = float("inf")

harmadik_index = 0
for i in range(1, len(eredmények_copy)):
    if eredmények_copy[i] < eredmények_copy[harmadik_index]:
        harmadik_index = i
eredmények_copy[harmadik_index] = float("inf")

print(f"1. helyezett: {nevek[elso_index]} ({eredmények[elso_index]} mp)")
print(f"2. helyezett: {nevek[masodik_index]} ({eredmények[masodik_index]} mp)")
print(f"3. helyezett: {nevek[harmadik_index]} ({eredmények[harmadik_index]} mp)")

# 9.f: Kik voltak gyorsabbak Gábornál?
gabor_index = nevek.index("Gábor")
gabor_ido = eredmények[gabor_index]

print("Gábortól gyorsabb emberek:")
for i in range(len(eredmények)):
    if eredmények[i] < gabor_ido:
        print(nevek[i])