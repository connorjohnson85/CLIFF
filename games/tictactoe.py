# text based only
from services.Speech import textTesting, textToSpeech, speechToText, inputTesting 

def printBoard(board):
    for boardLines in board:
        print('|'.join(boardLines))
            
def play(mode, board):
    move = inputTesting(mode, 'What is your move? ')
    textTesting(mode, move)
    move = int(move)
    if move <= 3:
        board[0][move-1] = 'x'
    if move <= 6 and move > 3:
        if move == 5:
            move = 1
        if move == 4:
            move = 0 
        if move == 6: 
            move = 2
        board[2][move] = 'x'
    if move > 6:
        if move == 7: 
            move = 0
        if move == 8:
            move = 1
        if move == 9: 
            move = 2
        board[4][move] = 'x'
    printBoard(board)
    computersMove(board)

def computersMove(board):
    mapping = []
    for row in board:
        if row != ['-','-','-']:
            for i in row:
                mapping.append(i)
    if mapping[0] == 'x' and mapping[1] == 'x' and mapping[2] != 'o':
        board[0][2] = 'o'
    elif mapping[0] == 'x' and mapping[2] == 'x' and mapping[1] != 'o':
        board[0][1] = 'o'
    elif mapping[3] == 'x' and mapping[4] == 'x' and mapping[5] != 'o':
        board[1][0] = 'o'
    if mapping[0] == 'x' and mapping[1] == 'x' and mapping[2] != 'o':
        board[0][2] = 'o'
    elif mapping[0] == 'x' and mapping[2] == 'x' and mapping[1] != 'o':
        board[0][1] = 'o'
    elif mapping[3] == 'x' and mapping[4] == 'x' and mapping[5] != 'o':
        board[1][0] = 'o'
    
    



def ticTacToe(mode):
    textTesting(mode, 'Welcome to Tic-Tac-Toe')
    board = [['#','#','#'],['-','-','-'], ['#','#','#'], ['-','-','-'], ['#','#','#']]
    mappingBoard = [['1','2','3'],['-','-','-'], ['4','5','6'], ['-','-','-'], ['7','8','9']]
    printBoard(board)
    print('')
    printBoard(mappingBoard)
    play(mode, board)


