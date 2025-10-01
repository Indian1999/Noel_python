print("Hello World!")

name = input("Add meg a neved: ")
print(type(name)) # <class 'str'> string, azaz szöveg típusú

print("Hello", name, "!")
print("Hello " + name + "!")
print(f"Hello {name}!")

age = int(input("Hány éves vagy? ")) # Az input eredménye mindig string
print(type(age)) # <class 'int'> integer, egész szám típus
if age > 12:
    print("Elég idős vagy")
else:
    print("Ez még fiatal")

answer = input("Van kutyád? (igen/nem): ")
if answer == "igen":
    has_dog = True
else:
    has_dog = False

print(type(has_dog)) # <class 'bool'> Boolean, logikai érték (igaz vagy hamis lehet)
print("Van kutyád:", has_dog)
