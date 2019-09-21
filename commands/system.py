
import datetime
from services.Speech import textToSpeech as ts
import os

def options():
    print('C.L.I.F.F: I can currently recognize speech, play tictactoe, set reminders, easter eggs, and talk!')

def currentTimeSilent():
    print(datetime.datetime.now().date(), datetime.datetime.now().time())

def currentTimeProduction():
    ts('The current time is: ' + datetime.datetime.now().date() + ' ' + datetime.datetime.now().time())

def command_line():
    print('Starting command line')
    running = True
    while running == True:
        command = input('$ ')
        if command == 'exit':
            running = False 
            break
        os.system(command)

def python_shell():
    print('Starting Python Shell')
    os.system('python3')

