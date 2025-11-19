def myFunction():
    print("""
⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁
""")


def pyramid(n):
    for i in range(1, n+1):
        print("#" * i)

# y = 2x + 3
def f(x):
    return 2*x + 3

value = pyramid(3)
print(value) # None

value = f(10)
print(value) # 23

def add(a, b):
    return a + b

print(add(5, 3)) # 8

def div(a, b): # <- itt az a és b Paraméterek
    return a / b

print(div(7, 3)) # Itt a 7 meg a 3 argumentumok
print(div(3, 7))

#print(div(5)) # TypeError: div() missing 1 required positional argument: 'b'
#print(div(3, 7, 10)) # TypeError: div() takes 2 positional arguments but 3 were given

def say_hello(name, greeting = "Hi"):
    print(f"{greeting} {name}!")

say_hello("Noel")   # Hi Noel!
say_hello("Szabolcs", "Szia") # Szia Szabolcs!


# Ha egy függvény return kulcsszó ér, akkor kilép a függvény
def func():
    print("Hello")
    return
    print("Szia")

func()


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


# Írjunk egy függvényt ami paraméterben 3 számot kap meg.
# Ez a három szám egy háromszög oldalainak a hossza
# A függvény egy logikai értéket ad vissza, igazat, ha derékszögű a háromszög
# Hamisat, ha nem

def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False

print(is_right_triangle(9, 12, 15))
print(is_right_triangle(15, 9, 12))
print(is_right_triangle(19, 12, 16))

# Írjunk egy függvényt amely paraméterben megkap egy listát, és visszaadja a lista elemeinek átlagát

def average(lista):
    összeg = 0
    for i in range(len(lista)):
        összeg += lista[i]
    return összeg / len(lista)

print(average([67,3,2,5,56,67,3,2,34,5,5,7,98,3,1,6]))



# 0. feladat: Írjunk egy függvényt amely egy számot kap meg paraméterben és visszaadja a szám 1000-szeresét

# 1. feladat: Írjunk egy függvényt amely egy stringet vár paraméterben, és egy egész számot ad vissza
# A függvény visszatérési értéke a paraméterben megkapott string magánhangzóinak száma

def vowels(string):
    counter = 0
    for char in string:
        if char in "öüóűúőoiueaéáíÓÜÖŰÚŐOIUEÁÉAÍ":
            counter += 1
    return counter

print(vowels("Kaparófa")) # 4 (mert 4 magánhangzó van a "Kaparófa" stringben)

# 2. feladat: Írjunk egy függvényt amely egy listát kap meg paraméterül és visszaadja a listában található
# legnagyobb elem értékét!

# 3. feladat: Írjunk egy függvényt amely egy háromszög 3 oldalának a hosszát kapja meg paraméterben
# és visszaad egy logikai értéket, hogy a háromszög, egyenlő szárú-e!

def egyenlo_szaru_e(a, b, c):
    if a == b or a == c or b == c:
        return True
    return False

print(egyenlo_szaru_e(3, 4, 5))
print(egyenlo_szaru_e(3, 4, 4))
print(egyenlo_szaru_e(3, 4, 3))
print(egyenlo_szaru_e(4, 4, 5))



