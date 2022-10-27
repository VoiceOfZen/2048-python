# Steps
# 1. Set up the board, using a list of lists. Create a temporary board.
# board = [
#     [0, 0, 2, 2],
#     [2, 2, 2, 2],
#     [4, 0, 0, 4],
#     [0, 2, 0, 0]
# ]
# 2. Create functions that will merge left, right, up, and down.
# Will create functions to reverse and transpose the list of lists to do this.
# 3. Set up the start of the game, creating an empty gameboard
# filled with two random values.
# 4. Set up the rounds of the game, where the user will have the option
# to merge in any one of the four directions, and after they move
# then new board will display.
# 5. Set up adding a new value each time.
# 6. Set up functions testing if the user has won or lost.

import random
import copy

board_size = 4


# This function will print out the current board in the way we want
def display():
    # Find out which value is the largest
    largest = board[0][0]
    for row_0 in board:
        for element in row_0:
            if element > largest:
                largest = element
    # Set the max number of spaces needed to the length of the largest value
    num_spaces = len(str(largest))

    for row_1 in board:
        curr_row = "|"
        for element in row_1:
            # If the current element is 0, add a space
            if element == 0:
                curr_row += " " * num_spaces + "|"
            # If not, we should add the value
            else:
                curr_row += (" " * (num_spaces - len(str(element)))) + str(element) + "|"
                # if num = odd => make it even to the bigger side like 3->4
                # just do + 1

                # odd_numbers = list(filter(lambda x: x % 2 == 1, number_list))
                # ...or just add 2 spaces on two sides since maximum number is 2048
                # And it won't get any bigger. but if it will... then yes
        # Print the generated row
        print(curr_row)
    print()


# This function merges one row left
def mergeOneRowL(row):
    # Move everything as far to the left as possible
    for j_mrl in range(board_size - 1):
        for i_mrl in range(board_size - 1, 0, -1):
            # Test if there is an empty space, move over if so
            if row[i_mrl - 1] == 0:
                row[i_mrl - 1] = row[i_mrl]
                row[i_mrl] = 0

    # Merge everything to the left
    for i_mrl in range(board_size - 1):
        if row[i_mrl] == row[i_mrl + 1]:
            row[i_mrl] *= 2
            row[i_mrl + 1] = 0

    # Move everything to the left again
    for i_mrl in range(board_size - 1, 0, -1):
        if row[i_mrl - 1] == 0:
            row[i_mrl - 1] = row[i_mrl]
            row[i_mrl] = 0
    return row


# This function merges the whole board to the left
def merge_left(current_board):
    # Merge every row in the board left
    for ml in range(board_size):
        current_board[ml] = mergeOneRowL(current_board[ml])
    return current_board


# This function reverses the order of one row
def reverse(row):
    # Add all elements of the row to a new list, in reverse order
    new = []
    for ir in range(board_size - 1, -1, -1):
        new.append((row_2[ir]))
        return new


# This function merges the whole board right
def merge_right(current_board):
    # Look at every row in the board
    for imr in range(board_size):
        # Reverse the row, merge to the left, then reverse back
        current_board[imr] = reverse(current_board[imr])
        current_board[imr] = mergeOneRowL(current_board)
        current_board[imr] = reverse(current_board[imr])
    return current_board


# This function transposes the whole board
def transpose(current_board):
    for jtr in range(board_size):
        for itr in range(jtr, board_size):
            if not itr == jtr:
                temp = current_board[jtr][itr]
                current_board[jtr][itr] = current_board[itr][jtr]
                current_board[itr][jtr] = temp
    return current_board


# This function merges the whole board up
def merge_up(current_board):
    # Transposes the whole board, merges it all left, then transposes it back
    current_board = transpose(current_board)
    current_board = merge_left(current_board)
    current_board = transpose(current_board)
    return current_board


# This function merges the whole board down
def merge_down(current_board):
    # Transposes the whole board, merges it all right, then transposes it back
    current_board = transpose(current_board)
    current_board = merge_right(current_board)
    current_board = transpose(current_board)
    return current_board


# This function picks a new value for the board
def pick_new_value():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2


# This function adds a value to the board in one of the empty spaces
def add_new_value():
    row_Num = random.randint(0, board_size - 1)
    col_Num = random.randint(0, board_size - 1)
    # Pick spots until we find one that is empty
    while not board[row_Num][col_Num] == 0:
        row_Num = random.randint(0, board_size - 1)
        col_Num = random.randint(0, board_size - 1)
    # Fill the empty spot with a new value
    board[row_Num][col_Num] = pick_new_value()


# This function tests if the user has one
def won():
    for won_i in board:
        if 2048 in won_i:
            return True
        return False


# This function tests if the user has lost
def noMoves():
    # Create two copies of the board
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)
    # Test every possible move
    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False




# display()

board = []
for i in range(board_size):
    row = []
    for j in range(board_size):
        row.append(0)
    board.append(row)

# Fill two spots with random values, to start the game
numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, board_size - 1)
    colNum = random.randint(0, board_size - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pick_new_value()
        numNeeded -= 1

print("Welcome to 2048! "
      "Your goal is to combine values to get the number 2048, "
      "by merging the board in different directions. "
      "Everytime, u will need to type 'd' to merge right, "
      "'w' to merge up, 'a' to merge left, and 's' to merge down. "
      "\n\n Here is the starting board: ")
display()

gameOver = False

# Repeat asking the user for new moves while the game isn't over
while not gameOver:
    move = input("Which way do u want to merge? ")

    # Assume they entered a valid input
    validInput = True

    # Create a copy of the board
    tempBoard = copy.deepcopy(board)
    # Figure out which way the person wants to merge
    # and use the correct function
    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        validInput = False
        # or u can change to random

    # if the input was not valid, they need to enter a new input,
    # so this round is over
    if not validInput:
        print("Your input was not valid, please try again")
    # Otherwise their input was valid
    else:
        # Test if their move was unsuccessful
        if board == tempBoard:
            # Tell them to try again
            print("Try a different direction!")
        else:
            # Test if the user has won
            if won():
                display()
                print("You Won!")
                gameOver = True
            else:
                # Add a new value
                add_new_value()
                display()
                # Figure out if they lost
                if noMoves():
                    print("Sorry, u have no possible moves, u lose!")
                    gameOver = True
