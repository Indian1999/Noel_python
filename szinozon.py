import random

def generate_puzzle(lower_bound = 1, upper_bound = 6, number_of_digits = 4):
    puzzle = ""  
    while len(puzzle) < number_of_digits:
        num = str(random.randint(lower_bound, upper_bound))
        if num not in puzzle:
            puzzle += num 
    return puzzle # A függvény visszatérési értéke

def ask_player(puzzle, lower_bound = 1, upper_bound = 6, number_of_digits = 4):
    tipp = input(f"Adj meg négy számjegyet ({lower_bound}-{upper_bound}) szóközek nélkül (pl.: {generate_puzzle(lower_bound, upper_bound, number_of_digits)})!\n")
    jo_szamok_rossz_helyen = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)): # i = 0, 1, 2, 3
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok_rossz_helyen += 1
    if jo_szamok_jo_helyen == number_of_digits:
        return False
    else:
        print("Jó számok jó helyen:", jo_szamok_jo_helyen)
        print("Jó számok, de rossz helyen:", jo_szamok_rossz_helyen)
        return True

def master_mind(lower_bound = 1, upper_bound = 6, number_of_digits = 4):
    puzzle = generate_puzzle(lower_bound, upper_bound, number_of_digits)
    gameOn = True
    tippek = 0
    while gameOn:
        gameOn = ask_player(puzzle, lower_bound, upper_bound, number_of_digits)
        tippek += 1
    print(f"Szép volt! {tippek} lépésből rájöttél, hogy a megoldás {puzzle} volt.")

