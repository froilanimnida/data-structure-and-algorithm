"""
Scenario:

Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you,
we've decided to simplify the game. Here are our assumptions:

    the computer (i.e., your program) should play the game using 'X's;
    the user (e.g., you) should play the game using 'O's;
    the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
    all the squares are numbered row by row starting with 1 (see the example session below for reference)
    the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it
    must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already
    occupied;
    the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends
    with a tie, you win, or the computer wins;
    the computer responds with its move and the check is repeated;
    don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for
    the game.

"""
import random

blocks = ["X" if x == 5 else x for x in range(1, 10)]

def computer_turn():
    while True:
        computer_choice = random.randint(0, 8)
        if blocks[computer_choice] in ["X", "O"]:
            continue
        else:
            blocks[computer_choice] = "X"
            winner_check(turn="user")
            break



def winner_check(turn):
    x_count = 0
    o_count = 0
    winner_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [2, 5, 8],
        [1, 4, 7],
        [0, 3, 6],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for positions in winner_positions:
        for combinations in positions:
            if blocks[combinations] == "X":
                x_count += 1
            elif blocks[combinations] == "O":
                o_count += 1

        if x_count == 3:
            render_board()
            print("Computer Wins.")
            break
        elif o_count == 3:
            render_board()
            print("User Wins.")
            break
        else:
            x_count = o_count = 0
    else:
        if turn == "computer":
            computer_turn()
        elif turn == "user":
            ask_for_number()



def render_board():
    row_strs = ["", "", "", "", ""]
    for i, block in enumerate(blocks):
        if i % 3 == 0:
            row_strs = ["", "", "", "", ""]
        row_strs[0] += "+---------+ "
        row_strs[1] += "|         | "
        row_strs[2] += f"|    {block}    | "
        row_strs[3] += "|         | "
        row_strs[4] += "+---------+ "
        if (i + 1) % 3 == 0:
            print("\n".join(row_strs))

def ask_for_number():
    render_board()
    while True:
        try:
            user_choice = int(input("Enter the cell number: "))
            if blocks[user_choice - 1] in ["X", "O"]:
                print("The cell is already occupied try again.")
                continue
            else:
                blocks[user_choice - 1] = "O"
                winner_check(turn="computer")
                break
        except ValueError:
            print("Please enter a valid value from 1-10")


ask_for_number()
