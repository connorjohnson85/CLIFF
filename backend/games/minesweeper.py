# text based only
import random
from services.Speech import textTesting, textToSpeech, speechToText, inputTesting 

# prints board
def printBoard(board):
    count = "00"
    for i in board:

        print(count , ' '.join(i))
        count = int(count)
        count  += 1
        if count <= 9:
            count = "0" + str(count)

mines = []

def minesweeper(mode): 
    # Gets the difficulty
    difficulty = inputTesting(mode, 'Easy, medium, or hard? ')
    length = inputTesting(mode, 'Small, Medium, or Large? ')
    textTesting(mode, "size of board: " + length + ' difficulty: ' + difficulty)
    # Sets the board using three predefined boards
    if length == 'small':
        sizeOfBoard = 8
        sizeFactor = 1
    if length == 'medium':
        sizeOfBoard = 12
        sizeFactor = 1.5
    if length == 'hard': 
        sizeOfBoard = 16
        sizeFactor = 2
    # Sets the difficulty using three predefined difficultys
    if difficulty == 'easy':
        mineFactor = 1
    if difficulty == 'medium':
        mineFactor = 2
    if difficulty == 'hard':
        mineFactor = 3 
    if False: 
        print(sizeOfBoard)

    # computes how many mines to place using the length, sizeFactor, and mineFactor
    for i in range(0, length * sizeFactor * mineFactor):
        i = i
        minerow = random.randint(1, length)
        minecol = random.randint(1, length)
        mines.append(minerow)
        mines.append(minecol)
    print(mines)
    
