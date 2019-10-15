# text based only
import random

emptyBoard = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]

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



class Ship: 
    def __init__(self, name, length, number):
        self.name = name
        self.length = length
        self.number = number
    
def ship(arrayOfShips):
    for item in arrayOfShips:
        print('{2} ({0}), ({1})'.format(item.length, item.number, item. name))
        for number in range(item.number):
            letter = input('Letter? ')
            col = int(input('Number? '))
            direction = int(input('Direction? '))
            rangeValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            row = rangeValues.index(letter.upper())
            board = emptyBoard
            board[col][row] = 'X'

            if direction == 1: 
                for i in range(item.length):
                    if board[col][row+i] == 'X':
                        print('Theres already a ship there!')
                    else:
                        for i in range(item.length):
                            board[col][row+i] = 'X'

                printBoard(board)

            if direction == 2:
                for i in range(item.length):
                    if board[col+i][row] == 'X':
                        print('Theres already a ship there!')
                        
                    else:
                        for i in range(item.length):
                            board[col+i][row] = 'X'
                printBoard(board)
            if direction == 3:
                for i in range(item.length):
                    board[col+i][row-i] = 'X'
                printBoard(board)
            if direction == 4:
                for i in range(item.length):
                    board[col+i][row+i] = 'X'
                printBoard(board)

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

def generateComputerBoard(emptyBoard):
    printBoard(emptyBoard)

def play():
    ships = [Ship('Battleship', 4, 1), Ship('Submarine', 3, 1), Ship('Pilot Boat', 2, 2)]
    placeShips(ships)

play()