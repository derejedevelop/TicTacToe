

def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def EnterMove(bo):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    val = int(input("Enter your move: "))

    while val not in MakeListOfFreeFields(bo):
        val = int(input("Enter your move: "))

    if val == 1:
        bo[0][0] = 'O'
    elif val == 2:
        bo[0][1] = 'O'
    elif val == 3:
        bo[0][2] = 'O'
    elif val == 4:
        bo[1][0] = 'O'
    elif val == 6:
        bo[1][2] = 'O'
    elif val == 7:
        bo[2][0] = 'O'
    elif val == 8:
        bo[2][1] = 'O'
    elif val == 9:
        bo[2][2] = 'O'

    return bo


def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers
    #
    freeField = []

    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                freeField.append(board[i][j])

    return freeField


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    from random import randrange
    val = randrange(10)

    while val not in MakeListOfFreeFields(board):
        val = randrange(10)

    if val == 1:
        board[0][0] = 'X'
    elif val == 2:
        board[0][1] = 'X'
    elif val == 3:
        board[0][2] = 'X'
    elif val == 4:
        board[1][0] = 'X'
    elif val == 6:
        board[1][2] = 'X'
    elif val == 7:
        board[2][0] = 'X'
    elif val == 8:
        board[2][1] = 'X'
    elif val == 9:
        board[2][2] = 'X'

    return board


br1 = [1, 2, 3]
br2 = [4, 'X', 6]
br3 = [7, 8, 9]

board = [br1, br2, br3]

DisplayBoard(board)
print(MakeListOfFreeFields(board))
DisplayBoard(EnterMove(board))
DisplayBoard(DrawMove(board))




