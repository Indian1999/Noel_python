# szöveget (karakterláncot) string (str) objektumban tárolunk

first_name = "Kis"
last_name = "Pista"
print(first_name + " " + last_name) # "Kis Pista"

szöveg = "a csillagok háborúja"
print(szöveg.upper()) # a szöveg minden karakterét nagybetűssé alakítja
print("AlmAFA".lower()) # kisbettűssé
print(szöveg.title()) # Minden szó első betűjét nagybetűsítiű
print(szöveg.capitalize()) # A legelső karaktert nagybetűsíti
print(szöveg.replace("a", "e"))
print("AlmAFA".replace("a", "e"))
print(szöveg.replace("ll", " kiscica "))

#num = input("Adj meg számot: ")
num = "54"
if num.isnumeric():
    print("num is numeric")
    num = int(num)
elif num.isdigit():
    print("num is digit")
    num = int(num)
elif "." in num and num.replace(".", "").isdigit():
    num = float(num)  
print(type(num))

szöveg = "A cica átsétált az úttesten, hogy felegyen egy lazacos szendvicset."
print(szöveg[0])
print(szöveg[3:6]) # Úgy működik mint a range (6. már nem lesz benne)
print(szöveg[:10]) # Elejétől a 10-ig
print(szöveg[7:])  # 7-től a legvégéig (utolsó is benne van)
print(szöveg[:])   # Egész
print(szöveg[-1])  # Hátulról a legelső    (.)
print(szöveg[-2])  # t
print(szöveg[5:-8])#
print(szöveg[9:3]) # Üres string
print(szöveg[9:3:-1]) #stá ac
print(szöveg[::5])   # Minden 5. karakter
print(szöveg[::-1])  # Fordítva a szöveg

# Számoljuk meg, hogy hány szóköz karakter van a stringben

counter = 0
for i in range(len(szöveg)):
    if szöveg[i] == " ":
        counter += 1
print("Szóközek száma:", counter)

counter = 0
for char in szöveg:
    if char == "a":
        counter += 1
print("Az 'a' karakterek száma:", counter)

print("Az 's' karakterek száma:", szöveg.count("s"))
print("Az első szóköz karakter indexe:", szöveg.find(" "))
print("Az első 'tt' karakterlánc indexe:", szöveg.find("tt"))
print("Van-e 'k' betű a szövegben?", "k" in szöveg)

lista = ["alma", "banán", "citrom", "dinnye"]
fruits = "".join(lista)  # lista elemeit ""-el elválasztva összefűzi
print(fruits)
fruits = " (kiscica) ".join(lista)  # lista elemeit " "-el elválasztva összefűzi
print(fruits)

# alt gr + Q   -> \        !=    / (Shift + 6)
# \n  -> enter karaktert jelöli
# Whitespace - Olyan karakter mint az enter, szóköz, tab
szöveg = "\n    \n    Ez itt egy\nTöbb soros\nstring változó.\n    "
print(szöveg)
szöveg = szöveg.strip() # Törli az elejéről és a végéről a whitespace karaktereket
print(szöveg)

sor = "alma;16;Peti;99;800;True"
items = sor.split(";")
print(items) # ['alma', '16', 'Peti', '99', '800', 'True']

# 1. feladat: Kérjünk be egy szöveget, és mentsük el egy változóba

# 2. feladat: Írjuk ki ennek a szövegnek a hosszát

# 3. feladat: Írjuk ki a szöveget visszafelé

# 4. feladat: Kérjünk be egy új stringet és számoljuk, hogy az hányszor szerepel az eredetiben

# 5. feladat: Számoljuk meg, hogy hány szó szerepel a szövegben.

# 6. feladat: Számold meg, hogy hány magánhangzó szerepel a szövegben.

# 7. feladat: Döntsük el a szövegről, hogy palindróm-e!
# Palindrom, ugyan az előre olvasva mint hátra (pl.: kajak, Indul a görög aludni)