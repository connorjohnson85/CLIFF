# text based only
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

def placeShip():
    

def placeShips():
    helper = input('enter 1 to start placing ships, enter 2 for help: ')
    if helper == '1':
        print('Battleship first (4), (1)')
        letter = input('Letter? ')
        col = int(input('Number? '))
        direction = int(input('Direction? '))
        rangeValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        row = rangeValues.index(letter.upper())
        board = emptyBoard
        board[row+1][col-1] = 'X'
        printBoard(board)
    elif helper == '2':
        print('The grid of battleship is built into a system of numbers and letters')
        print('In order to place a ship, it will tell you the number of spaces the ship takes up, and then how many of them you can place')
        print('You\'ll need to enter three values, the letter, the number, and the direction')
        print('1 means horizontal, 2 means vertical, 3 means diagonal left, and 4 means diagonal right')
        print("It will display the ship and ask if thats where you want to place it. You cannot place ships on top of eachother")
placeShips()