import random
from services.Speech import textTesting
from services.Speech import inputTesting
def rockpaperscissors(mode):

    choices = ['rock', 'paper', 'scissors']
    move = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
    computersMove = random.choice(choices)
    def wincheck(move, computersMove):
        if move == 'r':
            if computersMove == 'paper':
                textTesting(mode, 'You lose! Computer Chose Paper!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else: 
                    textTesting(mode, 'ok')
            if computersMove == 'scissors':
                textTesting(mode, 'You won! Computer Chose Scissors!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else: 
                    textTesting(mode, 'ok')
            if computersMove == 'rock':
                textTesting(mode, 'Tie! Computer Chose rocks!')
                newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                newcomputersMove = random.choice(choices)
                wincheck(newmove, newcomputersMove)
        elif move == 'p': 
            if computersMove == 'paper':
                textTesting(mode, 'Tie! Computer Chose Paper!')
                newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                newcomputersMove = random.choice(choices)
                wincheck(newmove, newcomputersMove)
            if computersMove == 'scissors':
                textTesting(mode, 'You lose! Computer Chose Scissors!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else: 
                    textTesting(mode, 'ok')
            if computersMove == 'rock':
                textTesting(mode, 'You win! Computer Chose rocks!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else: 
                    textTesting(mode, 'ok')
        elif move == 's':
            if computersMove == 'paper':
                textTesting(mode, 'You Won! Computer Chose Paper!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else:
                    textTesting(mode, 'ok')
            if computersMove == 'scissors':
                textTesting(mode, 'Tie! Computer Chose Scissors!')
                newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
                newcomputersMove = random.choice(choices)
                wincheck(newmove, newcomputersMove)
            if computersMove == 'rock':
                textTesting(mode, 'You Lose! Computer Chose rocks!')
                answer = inputTesting(mode, 'Play Again? (y,n): ')
                if answer == 'y': 
                    newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s)')
                    newcomputersMove = random.choice(choices)
                    wincheck(newmove, newcomputersMove)
                else: 
                    textTesting(mode, 'ok')
            
        else:
            textTesting(mode, 'That is not a move!')
            newmove = inputTesting(mode, 'rock, paper, or scissors? (r, p, s): ')
            newcomputersMove = random.choice(choices)
            wincheck(newmove, newcomputersMove)
    wincheck(move, computersMove)
