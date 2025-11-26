import random
board = [
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
]
gameOn = True
player_1_turn = True
winner = "draw"
against_computer = True
def tic_tac_toe():
    global board, gameOn, winner, player_1_turn, against_computer
    def show_board():
        print("# 1 2 3")
        print(f"1 {board[0][0]} {board[0][1]} {board[0][2]}")
        print(f"2 {board[1][0]} {board[1][1]} {board[1][2]}")
        print(f"3 {board[2][0]} {board[2][1]} {board[2][2]}")

    def read_and_put_symbol():
        if against_computer and player_1_turn == False:
            sor = random.randint(0, 2)
            oszlop = random.randint(0, 2)
            while board[sor][oszlop] != "-":
                sor = random.randint(0, 2)
                oszlop = random.randint(0, 2)
            board[sor][oszlop] = "O"
            return

        correct_placement = False
        while not correct_placement:
            sor = int(input("Adj meg egy sort (1-3): "))
            while sor < 1 or sor > 3:
                print("Nincs ilyen sor!")
                sor = int(input("Adj meg egy sort (1-3): "))
            oszlop = int(input("Adj meg egy oszlopot (1-3): "))
            while oszlop < 1 or oszlop > 3:
                print("Nincs ilyen oszlop!")
                oszlop = int(input("Adj meg egy oszlopot (1-3): "))

            if board[sor-1][oszlop-1] == "-":
                correct_placement = True
                if player_1_turn:
                    board[sor-1][oszlop-1] = "X"
                else:
                    board[sor-1][oszlop-1] = "O"
            else:
                print("Ez a pozíció már foglalt!")

    def check_for_win():
        global winner, gameOn # A globális térben lévő winner változót használd!
        # Sorok ellenőrzése
        for i in range(3): # i = 0, 1, 2
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "-":
                if player_1_turn:
                    winner = "X wins!"
                else:
                    winner = "O wins!"
                gameOn = False
                return

        # Oszlopok ellenőrzése
        for i in range(3): # i = 0, 1, 2
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != "-":
                if player_1_turn:
                    winner = "X wins!"
                else:
                    winner = "O wins!"
                gameOn = False
                return

        # Átlók ellenőrzése
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != "-":
            if player_1_turn:
                winner = "X wins!"
            else:
                winner = "O wins!"
            gameOn = False
            return
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != "-":
            if player_1_turn:
                winner = "X wins!"
            else:
                winner = "O wins!"
            gameOn = False
            return

        # Döntetlen ellenőrzése
        for row in board:
            if "-" in row:
                return
        gameOn = False
        winner = "Draw!"

    def which_player():
        if player_1_turn:
            print("X játékos következik!")
        else:
            print("O játékos következik!")

    answer = input("Számítógép ellen szeretnél játszani? (igen/nem)\n")
    if answer == "igen":
        against_computer = True
    else:
        against_computer = False

    while gameOn:
        show_board()
        which_player()
        read_and_put_symbol()
        check_for_win()
        player_1_turn = not player_1_turn

    show_board()
    print(winner)
