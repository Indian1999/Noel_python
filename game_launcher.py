from szinozon import master_mind

print("Üdvözöllek a játék launcherben!")
print("Játékok:")
print("1: Színözön")
print("2: Fortninte")
print("3: Minecraft")
print("4: Roblox")
print("5: Factorio")

answer = input("Add meg az indítani kívánt játék számát!\n")

if answer == "1":
    master_mind()