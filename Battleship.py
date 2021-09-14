import random
import os
clear = lambda: os.system('cls')
# Creating Board and Player Selection
board = []
board_size = 0

clear()
player_number = int(input("How many players are playing?(1-2): "))
while board_size < 1 or board_size > 10:
    board_size = int(input("Board Size(1-10): "))
    if board_size < 1 or board_size > 10:
        print ("Thats not between 1-10!")

if player_number == 2:
    for x in range(0,board_size):
      board.append(["~"] * board_size + ["|"] + ["~"] * board_size)

    def print_board(board):
        for row in board:
            print (" ".join(row))

if player_number == 1:
    for x in range(0,board_size):
      board.append(["~"] * board_size)

    def print_board(board):
        for row in board:
            print (" ".join(row))

print_board(board)


# Creating Battleships
if player_number == 1:
    player_select = "player"
    while player_select != "sink" and player_select != "hide":
        player_select = input("Do you want to sink or hide ships? (Choose 'sink' or 'hide'): ")
        if player_select != str("sink") and player_select != str("hide"):
            print ("That is not a valid playmode!")


    Number_Battleships = 0
    while Number_Battleships < 1 or Number_Battleships > 3:
        Number_Battleships = int(input("Number of Battleships(1-3): "))
        if Number_Battleships < 1 or Number_Battleships > 3:
            print ("Thats not between 1-3!")

    ship_row = []
    ship_column = []


    if player_select == "sink":
        if board_size >= Number_Battleships:
            ship_row = random.sample(range(len(board)), Number_Battleships)
            ship_column = random.sample(range(len(board)), Number_Battleships)
        if board_size < Number_Battleships:
            for ships in range(Number_Battleships):
                def random_row(board):
                    return random.randint(0, len(board) - 1)
                def random_column(board):
                    return random.randint(0, len(board) - 1)
                ship_row.append(random_row(board))
                ship_column.append(random_column(board))
            
    for ships in range(Number_Battleships):
        if player_select == "hide":
            sr = -1
            while sr < 0 or sr > ((board_size) - 1):
                sr = int(input("Hide your ship (row) between 0-" + str((board_size) - 1) + ": "))
                if sr < 0 or sr > ((board_size) - 1):
                    print ("Thats not between 0-" + str((board_size) - 1) + "!")
                if sr > 0 and sr < ((board_size) - 1):
                    ship_row.append(sr)
            sc = -1
            while sc < 0 or sc > ((board_size) - 1):
                sc = int(input("Hide your ship (column) between 0-" + str((board_size) - 1) + ": "))
                if sc < 0 or sc > ((board_size) - 1):
                    print ("Thats not between 0-" + str((board_size) - 1) + "!")
                if sc > 0 and sc < ((board_size) - 1):
                    ship_column.append(sc)

if player_number == 2:
    Number_Battleships = 0
    while Number_Battleships < 1 or Number_Battleships > 3:
        Number_Battleships = int(input("Number of Battleships(1-3): "))
        if Number_Battleships < 1 or Number_Battleships > 3:
            print ("Thats not between 1-3!")

    player_one_r = []
    player_one_c = []

    for ships in range(Number_Battleships):
        por = -1
        while por < 0 or por > board_size - 1:
            por = int(input("Player 1, hide your ship (row) between 0-" + str((board_size - 1)) + ": "))
            if por < 0 or por > board_size - 1:
                print ("Thats not between 0-" + str((board_size - 1)) + "!")
            if por > 0 and por < board_size - 1:
                player_one_r.append(por)
        poc = -1
        while poc < 0 or poc > board_size - 1:
            poc = int(input("Player 1, hide your ship (column) between 0-" + str((board_size - 1)) + ": "))
            if poc < 0 or poc > board_size - 1:
                print ("Thats not between 0-" + str((board_size - 1) )+ "!")
            if poc > 0 and poc < board_size - 1:
                player_one_c.append(poc)
    clear()

    player_two_r = []
    player_two_c = []

    for ships in range(Number_Battleships):
        ptr = -1
        while ptr < 0 or ptr > board_size - 1:
            ptr = int(input("Player 1, hide your ship (row) between 0-" + str((board_size) - 1) + ": "))
            if ptr < 0 or ptr > board_size - 1:
                print ("Thats not between 0-" + str((board_size - 1))+ "!")
            if ptr > 0 and ptr < board_size - 1:
                player_two_r.append(ptr)
        ptc = -1
        while ptc < 0 or ptc > board_size - 1:
            ptc = int(input("Player 1, hide your ship (column) between 0-" + str((board_size) - 1) + ": "))
            if ptc < 0 or ptc > board_size - 1:
                print ("Thats not between 0-" + str((board_size) - 1) + "!")
            if ptc > 0 and ptc < board_size - 1:
                player_two_c.append(ptc)
    clear()

# Turns/Guesses
if player_number == 1:
    if player_select == "sink":
        turn_number = int(input("How many turns do you want?: "))
        ships_hit = 0

        for turn in range(turn_number):
            print ("Turn #: " + str(turn + 1))
            turn += 1

            guess_row = int(input("Guess row (0-" + str(len(board) - 1) + "): "))
            guess_column = int(input("Guess column (0-" + str(len(board) - 1) + "): "))

            if Number_Battleships == 1:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if ships_hit == Number_Battleships:
                            print ("You win")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                if turn == turn_number:
                    print ("Game over")
                print_board(board)
                for i in range(Number_Battleships):
                    print ("My battleship was hidden at " + str(ship_row[i]) + "," + str(ship_column[i]))

            if Number_Battleships == 2:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]) or (guess_row == ship_row[1] and guess_column == ship_column[1]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if ships_hit == Number_Battleships:
                            print ("You win")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                if turn == turn_number:
                    print ("Game over")
                print_board(board)
                for i in range(Number_Battleships):
                    print ("My battleship was hidden at " + str(ship_row[i]) + "," + str(ship_column[i]))

            if Number_Battleships == 3:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]) or (guess_row == ship_row[1] and guess_column == ship_column[1]) or (guess_row == ship_row[2] and guess_column == ship_column[2]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if ships_hit == Number_Battleships:
                            print ("You win")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                if turn == turn_number:
                    print ("Game over")
                print_board(board)
                for i in range(Number_Battleships):
                    print ("My battleship was hidden at " + str(ship_row[i]) + "," + str(ship_column[i]))
    if player_select == "hide":
        turn_number = (2 * Number_Battleships)
        ships_hit = 0

        for turn in range(turn_number):
            print ("Turn #: " + str(turn + 1))
            turn += 1
            
            guess_row = (random.randint(1, len(board)))
            guess_column = (random.randint(1, len(board)))

            print (guess_row)
            print (guess_column)

            if Number_Battleships == 1:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]):
                    print ("I hit your battleship")
                    ships_hit += 1
                    board[guess_row - 1][guess_column - 1] = "H"
                    if ships_hit == Number_Battleships:
                        print ("I win")
                        break
                else:
                    board[guess_row - 1][guess_column - 1] = "X"
                    if turn == turn_number:
                        print ("I Lost")
                print_board(board)
            
            if Number_Battleships == 2:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]) or (guess_row == ship_row[1] and guess_column == ship_column[1]):
                    print ("I hit your battleship")
                    ships_hit += 1
                    board[guess_row - 1][guess_column - 1] = "H"
                    if ships_hit == Number_Battleships:
                        print ("I win")
                        break
                else:
                    board[guess_row - 1][guess_column - 1] = "X"
                    if turn == turn_number:
                        print ("I Lost")
                print_board(board)
            
            if Number_Battleships == 3:
                if (guess_row == ship_row[0] and guess_column == ship_column[0]) or (guess_row == ship_row[1] and guess_column == ship_column[1]) or (guess_row == ship_row[2] and guess_column == ship_column[2]):
                    print ("I hit your battleship")
                    ships_hit += 1
                    board[guess_row - 1][guess_column - 1] = "H"
                    if ships_hit == Number_Battleships:
                        print ("I win")
                        break
                else:
                    board[guess_row - 1][guess_column - 1] = "X"
                    if turn == turn_number:
                        print ("I Lost")
                print_board(board)

if player_number == 2:
    turn_number = int(input("How many turns do you want?: ")) * 2
    p1_ships_hit = 0
    p2_ships_hit = 0

    for turn in range(turn_number):
        if turn == 0:
            print (" ")
        if (turn % 2) != 0:
            print ("P1 Turn #: " + str(int((turn) / 2 + 1)))
            guess_row = int(input("Guess row (0-" + str(len(board) - 1) + "): "))
            guess_column = int(input("Guess column (0-" + str(len(board) - 1) + "): "))

            if Number_Battleships == 1:
                if ((guess_row) == player_two_r[0] and (guess_column) == player_two_c[0]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column + (len(board) + 1)] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column + (len(board) + 1)] == "~":
                        p1_ships_hit += 1
                        board[guess_row][guess_column + (len(board) + 1)] = "H"
                        if p1_ships_hit == Number_Battleships:
                            print ("Player One Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column + (len(board) + 1)] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column + (len(board) + 1)] = "X"
                        print ("You missed my battleship")
                print_board(board)

            if Number_Battleships == 2:
                if ((guess_row) == player_two_r[0] and (guess_column) == player_two_c[0]) or ((guess_row) == player_two_r[1] and (guess_column) == player_two_c[1]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column + (len(board) + 1)] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column + (len(board) + 1)] == "~":
                        p1_ships_hit += 1
                        board[guess_row][guess_column + (len(board) + 1)] = "H"
                        if p1_ships_hit == Number_Battleships:
                            print ("Player One Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column + (len(board) + 1)] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column + (len(board) + 1)] = "X"
                        print ("You missed my battleship")
                print_board(board)
            
            if Number_Battleships == 3:
                if ((guess_row) == player_two_r[0] and (guess_column) == player_two_c[0]) or ((guess_row) == player_two_r[1] and (guess_column) == player_two_c[1]) or ((guess_row) == player_two_r[2] and (guess_column) == player_two_c[2]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column + (len(board) + 1)] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column + (len(board) + 1)] == "~":
                        p1_ships_hit += 1
                        board[guess_row][guess_column + (len(board) + 1)] = "H"
                        if p1_ships_hit == Number_Battleships:
                            print ("Player One Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column + (len(board) + 1)] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column + (len(board) + 1)] = "X"
                        print ("You missed my battleship")
                print_board(board)



        if (turn % 2) == 0:
            print ("P2 Turn #: " + str(int(turn / 2) + 1))
            guess_row = int(input("Guess row (0-" + str(len(board) - 1) + "): "))
            guess_column = int(input("Guess column (0-" + str(len(board) - 1) + "): "))
        
            if Number_Battleships == 1:
                if (guess_row == player_one_r[0] and guess_column == player_one_c[0]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        p2_ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if p2_ships_hit == Number_Battleships:
                            print ("Player Two Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                print_board(board)
            
            if Number_Battleships == 2:
                if (guess_row == player_one_r[0] and guess_column == player_one_c[0]) or (guess_row == player_one_r[1] and guess_column == player_one_c[1]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        p2_ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if p2_ships_hit == Number_Battleships:
                            print ("Player Two Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                print_board(board)
            
            if Number_Battleships == 3:
                if (guess_row == player_one_r[0] and guess_column == player_one_c[0]) or (guess_row == player_one_r[1] and guess_column == player_one_c[1]) or (guess_row == player_one_r[2] and guess_column == player_one_c[2]):
                    print ("You hit a battleship")
                    if board[guess_row][guess_column] == "H":
                        print ("You guessed that already")
                    elif board[guess_row][guess_column] == "~":
                        p2_ships_hit += 1
                        board[guess_row][guess_column] = "H"
                        if p2_ships_hit == Number_Battleships:
                            print ("Player Two Wins")
                            print_board(board)
                            break
                else:
                    if (guess_row >= board_size or guess_row < 0) or (guess_column >= board_size or guess_column < 0):
                        print ("Thats not on the map")
                    elif (board[guess_row][guess_column] == "X"):
                        print ("You guessed that already")
                    else:
                        board[guess_row][guess_column] = "X"
                        print ("You missed my battleship")
                print_board(board)