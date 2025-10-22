# Olvassunk be és tároljunk el egy szöveget
szöveg = "A cica felmászott a fára"
# Írjuk ki hogy hány karakterből el a beolvasott szöveg
print(len(szöveg))
# Írjuk ki a szöveget visszafelé
print(szöveg[::-1])
# Hány magánhangzó szerepel a szövegben?
maganhangzok = "öüóűúőoiueaéáíÓÜÖŰÚŐOIUEÁÉAÍ"
szamlalo = 0
for char in szöveg:
    if char in maganhangzok:
        szamlalo += 1
print(szamlalo)

# Hanyadik indexű karakter az első 'a' betű a szövegben? Ha nincs, akkor -1-et írjunk ki
print(szöveg.find("a"))

hanyadik = -1
for i in range(len(szöveg)):
    if szöveg[i] == 'a':
        hanyadik = i
        break
print(hanyadik)

# Összetett feladat: Titkosírás
# a, cseréljük ki az összes 'a' vagy 'A' karaktert '@' karakterre
# b, a 't' és 'T' karakterek helyett rakjunk be egy '!'-t
# c, 'e', 'E' helyett rakjunk '3'-t
# d, 'o', 'O' helyett rakjunk '0'-t
# e, 'u', 'U' helyett rakjunk 'v'-t
# Minden nagy karaktert alakítsunk kisbetűsre
# A szöveg első felét helyezzük át a string elejéről a végére
# Írjuk ki az így kapott szöveget

új_szöveg = szöveg.replace("a", "@")
új_szöveg = új_szöveg.replace("A", "@")
új_szöveg = új_szöveg.replace("t", "!")
új_szöveg = új_szöveg.replace("T", "!")
új_szöveg = új_szöveg.replace("e", "3")
új_szöveg = új_szöveg.replace("E", "3")
új_szöveg = új_szöveg.replace("o", "0")
új_szöveg = új_szöveg.replace("O", "0")
új_szöveg = új_szöveg.replace("u", "v")
új_szöveg = új_szöveg.replace("U", "v")
új_szöveg = új_szöveg.lower()
hossz = len(új_szöveg)
új_szöveg = új_szöveg[hossz//2:] + új_szöveg[:hossz//2]
print(új_szöveg)
