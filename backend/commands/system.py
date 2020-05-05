import datetime
from services.Speech import textToSpeech as ts, inputTesting, textTesting
import os
import time
import datetime
#
# All System functions are stored in this folder
# Anything that involves the main cpu or the body of cliff is stored here
#

globalPath = '/home/connor/CLIFF/CLIFF'

def stopwatch(mode):
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        textTesting(mode, "Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
    input("Press Enter to start stopwatch")
    start_time = time.time()
    input("Press Enter to stop stopwatch")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

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
        if command == '':
            print("You have to put in a command!")
        if 'cd' in command:
                directory = command.split(" ")[1]
                try:
                        os.chdir(directory)
                except FileNotFoundError:
                        os.system("echo 'directory doesn\'t exist'")
        else:
                os.system(command)

# Starts a python shell instance. Used more for debugging than anything else
def python_shell():
    print('Starting Python Shell')
    os.system('python3')

def network_diagonistics():
    os.system('ping google.com -c 10 | grep \'packets\'')

def system_diagonistics():
    os.system('top | grep \'Processes\' -a')
    os.system('du -c | grep \'total\'')
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

def createProject(mode, projectName):
    path = globalPath

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
    os.chdir('{0}/projects/{1}'.format(globalPath, projectName))
    textTesting(mode, 'directory changed into project {}'.format(projectName))

def closeProject(mode):
    os.chdir(globalPath)

def openNote(mode, note):
    try:
        newNote = open(note, 'r')
        textTesting(mode, newNote.read())
        newNote.close()
    except FileNotFoundError:
        textTesting(mode, '{} doesn\'t exist'.format(note))
  
def createNote(mode):
    name = inputTesting(mode, 'What would you like the title of the note to be? ')
    line = inputTesting(mode, 'What would you like the note to say? ')
    newFile = open('{0}/journals/notes/{1}'.format(globalPath, name), 'w+')
    newFile.write(line)
    newFile.close()

def listNotes(mode):
    notes = []
    os.chdir('{0}/journals/notes'.format(globalPath))
    os.system('ls')
    os.chdir(globalPath)

def deleteNote(mode, name):
    try:
        print(globalPath)
        os.remove('{0}/journals/notes/{1}'.format(globalPath,name))
        
    except FileNotFoundError:
        textTesting(mode, '{} not found'.format(name))

def appendNote(mode, note):
    try:
        newNote = open(note, 'a+')
    except FileNotFoundError:
        textTesting(mode, 'Note not found')

def timer(mode, time):
    print(time)
