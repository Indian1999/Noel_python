import random

def generate_puzzle():
    puzzle = ""  
    while len(puzzle) < 4:
        num = str(random.randint(1, 6))
        if num not in puzzle:
            puzzle += num 
    return puzzle # A függvény visszatérési értéke

def ask_player(puzzle):
    tipp = input("Adj meg négy számjegyet (1-6) szóközek nélkül (pl.: 2134)!\n")
    jo_szamok_rossz_helyen = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)): # i = 0, 1, 2, 3
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok_rossz_helyen += 1
    if jo_szamok_jo_helyen == 4:
        return False
    else:
        print("Jó számok jó helyen:", jo_szamok_jo_helyen)
        print("Jó számok, de rossz helyen:", jo_szamok_rossz_helyen)
        return True

def master_mind():
    puzzle = generate_puzzle()
    gameOn = True
    tippek = 0
    while gameOn:
        gameOn = ask_player(puzzle)
        tippek += 1
    print(f"Szép volt! {tippek} lépésből rájöttél, hogy a megoldás {puzzle} volt.")

