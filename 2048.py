board = [
    [0, 0, 2, 2],
    [2, 2, 2, 2],
    [4, 0, 0, 4],
    [0, 2, 0, 0]
]
boardSize = 4


def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + "|"
            else:
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()


# This function merges one row left
def mergeOneRowL(row):
    # Move everything as far to the left as possible
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            # Test if there is an empty space, move over if so
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
    # Merge everything to the left
    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    # Move everything to the left again
    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


# This function merges the whole board to the left
def merge_left(currentBoard):
    # Merge every row in the board left
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard


merge_left(board)
display()
