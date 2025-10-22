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

# 9.b: Ki nyerte a versenyt?

# 9.c: Ki futott be utoljára?

# 9.d: Írjuk ki az első három helyezett nevét (és hogy hanyadik lett)!