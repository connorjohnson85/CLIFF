import datetime
from services.Speech import textToSpeech as ts
import os

#
# All System functions are stored in this folder
# Anything that involves the main cpu or the body of cliff is stored here
#

def options():
    print('C.L.I.F.F: I can currently recognize speech, play tictactoe, set reminders, easter eggs, run system and network diagonistics, and talk!')

def currentTimeSilent():
    # Gets the current date
    print(datetime.datetime.now().date(), datetime.datetime.now().time())

def currentTimeProduction():
    ts('The current time is: ' + datetime.datetime.now().date() + ' ' + datetime.datetime.now().time())

def currentTimeWebsite():
    return 'The current time is: ' + str(datetime.datetime.now().date()) + ' ' + str(datetime.datetime.now().time())

def command_line():
    # Starts a command line instance. Useful for debugging and potential linux users
    print('Starting command line')
    running = True
    while running == True:
        command = input('$ ')
        if command == 'exit':
            running = False 
            break
        os.system(command)

# Starts a python shell instance. Used more for debugging than anything else
def python_shell():
    print('Starting Python Shell')
    os.system('python3')

def network_diagonistics():
    os.system('ping google.com -c 10 | grep \'packets\'')

def system_diagonistics():
    os.system('top -l1 | grep Processes -a10')
    network_diagonistics()
