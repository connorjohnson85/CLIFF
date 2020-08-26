# text based only
import random
from services.Speech import textTesting, textToSpeech, speechToText, inputTesting 

# Prints boards
def printBoard(board):
    for boardLines in board:
        print('|'.join(boardLines))

# Gets players Move
def playersMove(mode, board): 
    move = inputTesting(mode, 'What is your move? ')
    textTesting(mode, move)
    move = int(move)
    if move <= 3 and board[0][move-1] != 'o' and board[0][move-1] != 'x':
        board[0][move-1] = 'x'
    if move <= 6 and move > 3:
        if move == 5:
            move = 1
        if move == 4:
            move = 0 
        if move == 6: 
            move = 2
        if board[2][move] != 'o' and board[2][move] != 'x':
            board[2][move] = 'x'
        else: 
            print('That was not a valid move!')
            playersMove(mode, board)
    if move > 6:
        if move == 7: 
            move = 0
        if move == 8:
            move = 1
        if move == 9: 
            move = 2
        if board[4][move] != 'o' and board[4][move] != 'x':
            board[4][move] = 'x'
        else:
            print('That was not a valid move!')
            playersMove(mode, board)

# Main play function
def play(mode, board):
    moves = 1 
    playersMove(mode, board)
    moves += 1 
    computersMove(board)
    moves += 1 
    printBoard(board)
    # Recursivly calls it till moves = 9
    if moves < 9:
        play(mode, board)

# Computers move 
def computersMove(board):
    mapping = []
    for row in board:
        if row != ['-','-','-']:
            for i in row:
                mapping.append(i)
    result = computerWinCheck(mapping, board)
    playerWinCheck(result, mapping, board)

def computerWinCheck(mapping, board):
        
    # Checks Row 1 to see if it can win
    if mapping[0] == 'o' and mapping[1] == 'o' and mapping[2] != 'x':
            board[0][1] = 'o'
    elif mapping[0] == 'o' and mapping[2] == 'o' and mapping[1] != 'x':
        board[0][1] = 'o'
    elif mapping[2] == 'x' and mapping[1] == 'x' and mapping[0] != 'o':
        board[0][0] = 'o'
    # Checks Row 2 to see if it can win
    elif mapping[3] == 'o' and mapping[4] != 'x' and mapping[5] == 'o':
        board[2][1] = 'o'
    elif mapping[3] != 'x' and mapping[4] == 'o' and mapping[5] == 'o':
        board[2][0] = 'o'
    elif mapping[3] == 'o' and mapping[4] == 'o' and mapping[5] != 'x':
        board[2][2] = 'o'
    # Checks Row 3 to see if it can win
    elif mapping[6] == 'o' and mapping[7] == 'o' and mapping[8] != 'x':
        board[4][2] = 'o'
    elif mapping[6] == 'o' and mapping[7] != 'x' and mapping[8] == 'o':
        board[4][1] = 'o'
    elif mapping[6] != 'x' and mapping[7] == 'o' and mapping[8] == 'o':
        board[4][0] = 'o'
    # Checks Column 1 to see if it can win 
    elif mapping[0] == 'o' and mapping[3] == 'o' and mapping[6] != 'x':
        board[4][0] = 'o'
    elif mapping[0] != 'x' and mapping[3] == 'o' and mapping[6] == 'o':
        board[0][0] = 'o'
    elif mapping[0] == 'o' and mapping[3] != 'x' and mapping[6] == 'o':
        board[2][0] = 'o'
    # Checks Column 2 to see if it can win 
    elif mapping[1] == 'o' and mapping[4] == 'o' and mapping[7] != 'x':
        board[4][1] = 'o'
    elif mapping[1] == 'o' and mapping[4] != 'x' and mapping[7] == 'o':
        board[2][1] = 'o'
    elif mapping[1] != 'x' and mapping[4] == 'o' and mapping[7] == 'o':
        board[0][1] = 'o'
    # Checks Column 3 to see if it can win 
    elif mapping[2] == 'o' and mapping[5] == 'o' and mapping[8] != 'x':
        board[4][2] = 'o'
    elif mapping[2] == 'o' and mapping[5] != 'x' and mapping[8] == 'o':
        board[2][2] = 'o'
    elif mapping[3] != 'x' and mapping[4] == 'o' and mapping[5] == 'o':
        board[0][2] = 'o'
    # Checks Diagonal 1 to see if it can win
    elif mapping[0] != 'x' and mapping[4] == 'o' and mapping[8] == 'o':
        board[0][0] = 'o'
    elif mapping[0] == 'o' and mapping[4] != 'x' and mapping[8] == 'o':
        board[2][1] = 'o'
    elif mapping[0] == 'o' and mapping[4] == 'o' and mapping[8] != 'x':
        board[4][2] = 'o'
    # Checks Diagonal 2 to see if it can win 
    elif mapping[2] == 'o' and mapping[4] == 'o' and mapping[6] != 'x':
        board[4][0] = 'o'
    elif mapping[2] == 'o' and mapping[4] != 'x' and mapping[6] == 'o':
        board[2][1] = 'o'
    elif mapping[3] != 'x' and mapping[4] == 'o' and mapping[5] == 'o':
        board[0][2] = 'o'
    else:
        return False

def playerWinCheck(result, mapping, board):
    if result == False:
        print(result)
        # Checks Row 1 to see if the player can win
        if mapping[0] == 'x' and mapping[1] == 'x' and mapping[2] != 'o':
            board[0][2] = 'o'
        elif mapping[0] == 'x' and mapping[2] == 'x' and mapping[1] != 'o':
            board[0][1] = 'o'
        elif mapping[2] == 'x' and mapping[1] == 'x' and mapping[0] != 'o':
            board[0][0] = 'o'
        # Checks Row 2 to see if the player can win
        elif mapping[3] == 'x' and mapping[4] != 'o' and mapping[5] == 'x':
            board[2][1] = 'o'
        elif mapping[3] != 'o' and mapping[4] == 'x' and mapping[5] == 'x':
            board[2][0] = 'o'
        elif mapping[3] == 'x' and mapping[4] == 'x' and mapping[5] != 'o':
            board[2][2] = 'o'
        # Checks Row 3 to see if the player can win
        elif mapping[6] == 'x' and mapping[7] == 'x' and mapping[8] != 'o':
            board[4][2] = 'o'
        elif mapping[6] == 'x' and mapping[7] != 'o' and mapping[8] == 'x':
            board[4][1] = 'o'
        elif mapping[6] != 'o' and mapping[7] == 'x' and mapping[8] == 'x':
            board[4][0] = 'o'
        # Checks Column 1 to see if the player can win
        elif mapping[0] == 'x' and mapping[3] == 'x' and mapping[6] != 'o':
            board[4][0] = 'o'
        elif mapping[0] == 'x' and mapping[3] != 'o' and mapping[6] == 'x':
            board[2][0] = 'o'
        elif mapping[0] != 'o' and mapping[3] == 'x' and mapping[6] == 'x':
            board[0][0] = 'o'
        # Checks Column 2 to see if the player can win 
        elif mapping[1] == 'x' and mapping[4] == 'x' and mapping[7] != 'o':
            board[4][1] = 'o'
        elif mapping[1] == 'x' and mapping[4] != 'o' and mapping[7] == 'x':
            board[2][1] = 'o'
        elif mapping[1] != 'o' and mapping[4] == 'x' and mapping[7] == 'x':
            board[0][1] = 'o'
        # Checks Column 3 to see if the player can win
        elif mapping[2] == 'x' and mapping[5] == 'x' and mapping[8] != 'o':
            board[4][2] = 'o'
        elif mapping[2] == 'o' and mapping[5] != 'o' and mapping[8] == 'x':
            board[2][2] = 'o'
        elif mapping[2] != 'o' and mapping[5] == 'x' and mapping[8] == 'x':
            board[0][2] = 'o'
        # Checks Diagonal 1 to see if the player can win
        elif mapping[2] == 'x' and mapping[4] != 'o' and mapping[6] == 'x':
            board[2][1] = 'o'
        elif mapping[2] == 'x' and mapping[4] == 'x' and mapping[6] != 'o':
            board[4][0] = 'o'
        elif mapping[2] != 'o' and mapping[4] == 'x' and mapping[6] == 'x':
            board[0][2] = 'o'
        # Checks Diagonal 2 to see if the player can win
        elif mapping[0] == 'x' and mapping[4] == 'x' and mapping[8] != 'o':
            board[4][2] = 'o'
        elif mapping[0] == 'x' and mapping[4] != 'o' and mapping[8] == 'x':
            board[2][1] = 'o'
        elif mapping[0] != 'o' and mapping[4] == 'x' and mapping[8] == 'x':
            board[0][0] = 'o'
        # Else: Checks all four corners. If all the corners are filled, randomly select an edge. if all edges are selected, find a 
        elif mapping[0] == '#' or mapping[2] == '#' or mapping[6] == '#' or mapping[8] == '#':
            choice = random.choice(['0', '2', '6', '8'])
            while mapping[int(choice)] != '#':
                choice = random.choice(['0', '2', '6', '8'])
            if mapping[int(choice)] == '#':
                if choice == '0':
                    board[0][0] = 'o'
                elif choice == '2':                        
                    board[0][2] = 'o'
                elif choice == '6':
                    board[4][0] = 'o'
                elif choice == '8':
                    board[4][2] = 'o'
        elif mapping[1] == '#' or mapping[3] == '#' or mapping[5] == '#' or mapping[7] == '#':
            choice = random.choice(['0', '2', '6', '8'])
            while mapping[int(choice)] != '#':
                choice = random.choice(['1', '3', '5', '7'])
            if mapping[int(choice)] == '#':
                if choice == '0':
                    board[0][0] = 'o'
                elif choice == '2':                        
                    board[0][2] = 'o'
                elif choice == '6':
                    board[4][0] = 'o'
                elif choice == '8':
                    board[4][2] = 'o'
        elif mapping[4] == '#':
            board[2][1] = 'o'
        # Check all corners, if one corner empty, fill that corner, if two or more corners 
        # open, randomly pick between them else, pick an edge, if edges are filled, pick center

def ticTacToe(mode):
    textTesting(mode, 'Welcome to Tic-Tac-Toe')
    board = [['#','#','#'],['-','-','-'], ['#','#','#'], ['-','-','-'], ['#','#','#']]
    mappingBoard = [['1','2','3'],['-','-','-'], ['4','5','6'], ['-','-','-'], ['7','8','9']]
    printBoard(board)
    print('')
    printBoard(mappingBoard)
    play(mode, board)

# Sees if anyone has won
def winCheck(mapping, mode):
    # Rows player
    if mapping[0] == 'x' and mapping[1] == 'x' and mapping[2] == 'x':
        playerWinMessage(mode)
    elif mapping[3] == 'x' and mapping[4] == 'x' and mapping[5] == 'x':
        playerWinMessage(mode)
    elif mapping[6] == 'x' and mapping[7] == 'x' and mapping[8] == 'x':
        playerWinMessage(mode)
    # Rows computer
    elif mapping[3] == 'o' and mapping[4] == 'o' and mapping[5] == 'o':
         computerWinMessage(mode)
    elif mapping[0] == 'o' and mapping[1] == 'o' and mapping[2] == 'o':
        computerWinMessage(mode)
    elif mapping[6] == 'o' and mapping[7] == 'o' and mapping[8] == 'o':
         computerWinMessage(mode)
    # Columns Player 
    # elif mapping[6] == 'x' and mapping[7] == 'x' and mapping[8] != 'o':
    #     board[4][2] = 'o'
    # elif mapping[6] == 'x' and mapping[7] != 'o' and mapping[8] == 'x':
    #     board[4][1] = 'o'
    # elif mapping[6] != 'o' and mapping[7] == 'x' and mapping[8] == 'x':
    #     board[4][0] = 'o'
    # # Columns Computer
    # elif mapping[0] == 'x' and mapping[3] == 'x' and mapping[6] != 'o':
    #     board[4][0] = 'o'
    # elif mapping[0] == 'x' and mapping[3] != 'o' and mapping[6] == 'x':
    #     board[2][0] = 'o'
    # elif mapping[0] != 'o' and mapping[3] == 'x' and mapping[6] == 'x':
    #     board[0][0] = 'o'
    # # Diagonals player
    # elif mapping[1] == 'x' and mapping[4] == 'x' and mapping[7] != 'o':
    #     board[4][1] = 'o'
    # elif mapping[1] == 'x' and mapping[4] != 'o' and mapping[7] == 'x':
    #     board[2][1] = 'o'

    # # Diagonals computer
    # elif mapping[2] == 'x' and mapping[5] == 'x' and mapping[8] != 'o':
    #     board[4][2] = 'o'
    # elif mapping[2] == 'o' and mapping[5] != 'o' and mapping[8] == 'x':
    #     board[2][2] = 'o'

# prints player win message
def playerWinMessage(mode):
    print('Player1 Wins!')
    if input('Play Again?(Y/N)').lower() == 'y':
        ticTacToe(mode)

# Prints computer win message
def computerWinMessage(mode):
    print('Computer Wins!')
    if input('Play Again?(Y/N)').lower() == 'y':
        ticTacToe(mode)

