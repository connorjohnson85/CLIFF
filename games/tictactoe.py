# text based only
from services.Speech import textTesting, textToSpeech, speechToText, inputTesting 

def printBoard(board):
    for boardLines in board:
        print('|'.join(boardLines))
            
def play(mode, board):
    move = inputTesting(mode, 'What is your move? ')
    textTesting(mode, move)
    


def ticTacToe(mode):
    textTesting(mode, 'Welcome to Tic-Tac-Toe')
    board = [['#','#','#'],['-','-','-'], ['#','#','#'], ['-','-','-'], ['#','#','#']]
    mappingBoard = [['1','2','3'],['-','-','-'], ['4','5','6'], ['-','-','-'], ['7','8','9']]
    printBoard(board)
    print('')
    printBoard(mappingBoard)
    play(mode, board)


