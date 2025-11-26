from szinozon import master_mind
from tic_tac_toe import tic_tac_toe
print("Üdvözöllek a játék launcherben!")
print("Játékok:")
print("1: Színözön")
print("2: Tic Tac Toe")
print("3: Minecraft")
print("4: Roblox")
print("5: Factorio")

answer = input("Add meg az indítani kívánt játék számát!\n")

if answer == "1":
    difficulty = input("Hanyas nehézségen akarsz játszani? (1-5)\n")
    if difficulty == "1":
        master_mind(1, 5, 4)
    elif difficulty == "2":
        master_mind(1, 7, 4)
    elif difficulty == "3":
        master_mind(1, 9, 4)
    elif difficulty == "4":
        master_mind(1, 9, 5)
    elif difficulty == "5":
        master_mind(1, 9, 6)
if answer == "2":
    tic_tac_toe()