import datetime
from services.Speech import textToSpeech as ts, inputTesting, textTesting
import os

#
# All System functions are stored in this folder
# Anything that involves the main cpu or the body of cliff is stored here
#

def options():
    print('C.L.I.F.F: I can currently recognize speech, play tictactoe, set reminders, easter eggs, run system and network diagonistics, and talk!')

def currentTimeSilent():
    # Gets the current date
    print(''.join(str(datetime.datetime.now()).split('.')[:-1]))

def currentTimeProduction():
    ts('The current time is: ' ''.join(str(datetime.datetime.now()).split('.')[:-1]))

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
    os.system('du -c | grep total')
    network_diagonistics()

def clearFile(mode, file):
    file = open(file, 'w+')
    file.close()
    textTesting(mode, 'File Cleared')

def readFile(mode, file):
    file = open(file, 'r')
    textTesting(mode, file.read())
    file.close()

def createFile(mode, file):
    file = open(file, 'w+')
    file.close()
    textTesting(mode, 'File Created')
    
def writeFile(mode, file):
    file = open(file, 'a+')
    opener = True
    while opener == True:    
        line = inputTesting(mode, 'What would you like to write into the file? ')
        if line == 'exit':
            file.close()
            break
        file.write(line)

    file.close()

def createProject(projectName):
    path = os.getcwd()
    path += '/projects/' + projectName
    try: 
        os.mkdir(path)
        file = open(path + '/LogFile.txt', 'w+')
        file.write('A basic Log File. Used to log errors so they don\'t display on the main console')
        file.close()
        file = open(path + '/main.py', 'w+')
        file.write('''# A basic main.py template file. imports my most commonly used basic modules.
import random
import math
import os


# Your main function class goes here
def main():
    print('Filler Code')
''')
        file.close()
    except OSError:
       textTesting(mode,'Creation of Project %s failed' % projectName)
    else:
        textTesting(mode, 'Successfully created Project %s' % projectName)

def openProject(mode, projectName):
    os.chdir('/Users/robinhansen/CLIFF/projects/{}'.format(projectName))
    textTesting(mode, 'directory changed into project {}'.format(projectName))

def closeProject(mode):
    os.chdir('/Users/robinhansen/CLIFF')