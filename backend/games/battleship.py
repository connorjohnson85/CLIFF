# text based only
import random

# Initializes an empty ten by ten board
emptyBoard = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

# Defines how to print the board
def printBoard(board): 
    count = '-1'
    for row in board:
        if int(count) < 9:
            count = '0' + str(int(count) + 1)
        else: 
            count = int(count) + 1 
        if int(count != '00'):
            print(count, ' '.join(row))
        else:
            print('  ', ' '.join(row))

printBoard(emptyBoard)


# Defines a ship object
class Ship: 
    def __init__(self, name, length, number):
        self.name = name
        self.length = length
        self.number = number
    
# Places a ship
def placeShip(row, col, direction, checker, item):
    if checker == False: 

        # Checks the horizontal direction(right)
        if direction == 1:
            for i in range(item.length):
                    board[col][row+i] = 'X'
        
        # Checks the vertical direction(down)
        if direction == 2:
            for i in range(item.length):
                board[col+i][row]

        # Checks the diagonal direction(left)
        if direction == 3:
            for i in range(item.length):
                board[col+i][row-i] = 'X'
            
        # Checks the diagonal direction(right)
        if direction == 4:
            for i in range(item.length):
                board[col+i][row+i] = 'X'
        
    else:
        shipController(item)
    printBoard(board)

# Main ship controller function, gets the list of ship, and collects where the player wants to store them
def shipController(item):
        # Prints the number of items, the length, and the name
        print('Name: {2} Length: ({0}), Number: ({1})'.format(item.length, item.number, item. name))
                    board = emptyBoard
        for number in range(item.number):
            # Gets user input where to place the ship
            letter = input('Letter? ')
            col = int(input('Number? '))
            direction = int(input('Direction? '))

            rangeValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            row = rangeValues.index(letter.upper())
            
            # places an X on the board
            board[col][row] = 'X'
            shipThere = False

            # Checks to make sure that no ships are there
            for i in range(item.length):
                if board[col][row+i] == 'X':
                    shipThere = True
            
            for i in range(item.length):
                print(board[col+1][row])
                if board[col+i][row] == 'X':
                    shipThere = True

            for i in range(item.length):
                if board[col+i][row-i] == 'X':
                    shipThere = True

            for i in range(item.length):
                if board[col+i][row+i] == 'X':
                    shipThere = True
                    
            placeShip(col, row, direction, shipThere, item)
            printBoard(board)

# for each item in the array, calls shipController
def ship(arrayOfShips):
     for item in arrayOfShips:
        shipController(item)

# start function. Gets computer board
def placeShips(ships):
    helper = input('enter 1 to start placing ships, enter 2 for help: ')
    if helper == '1':
        ship(ships)
    elif helper == '2':
        print('The grid of battleship is built into a system of numbers and letters')
        print('In order to place a ship, it will tell you the number of spaces the ship takes up, and then how many of them you can place')
        print('You\'ll need to enter three values, the letter, the number, and the direction')
        print('1 means horizontal, 2 means vertical, 3 means diagonal left, and 4 means diagonal right')
        print("It will display the ship and ask if thats where you want to place it. You cannot place ships on top of eachother")

# Generates computer board to be used
def generateComputerBoard(emptyBoard):
    printBoard(emptyBoard)

# play function, initializes all ships
def play():
    ships = [Ship('Battleship', 4, 1), Ship('Submarine', 3, 1), Ship('Pilot Boat', 2, 2)]
    placeShips(ships)

play()