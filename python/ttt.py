def renderBoard():
    # This function clears terminal, prints out the board
    print('\033[H\033[J')
    print(' ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]))
    print('-----------')
    print(' ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]))
    print('-----------')
    print(' ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]))
    print currentPlayer + "'s turn now"

def switchTurn():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    # What's another way you can keep track of the turn?

def processInput():
    global board
    renderBoard()
    choice = raw_input("Make a selection: ")
    valid_input = False
    while not valid_input:
        if ["1", "2", "3", "4", "5", "6", "7", "8", "9"].__contains__(choice) and choice != "":
            if board[int(choice) - 1] == "X" or board[int(choice)- 1] == "O":
                renderBoard()
                choice = raw_input("Can't do that. Try something else: ")
            else:
                board[int(choice) - 1] = currentPlayer
                switchTurn()
                valid_input = True
        else:
            renderBoard()
            choice = raw_input("Can't do that. Try something else: ")

def checkWinner():
    global gameOver
    if board[0] == board[1] == board[2]:
        gameOver = True
    if board[3] == board[4] == board[5]:
        gameOver = True
    if board[6] == board[7] == board[8]:
        gameOver = True
    if board[0] == board[3] == board[6]:
        gameOver = True
    if board[1] == board[4] == board[7]:
        gameOver = True
    if board[2] == board[5] == board[8]:
        gameOver = True
    if board[0] == board[4] == board[8]:
        gameOver = True
    if board[2] == board[4] == board[6]:
        gameOver = True


def playGame():
    global board, gameOver, currentPlayer
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    gameOver = False
    currentPlayer = "X"
    while not gameOver:
        processInput()
        checkWinner()
    switchTurn()
    renderBoard()
    print currentPlayer + " is the winner!"

playGame()
