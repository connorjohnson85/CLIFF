import commands.mymath as mymath
import commands.system as system
import commands.productivity as productivity
import commands.protocols as protocol
from services.Speech import textToSpeech as textToSpeech, textTesting, inputTesting
import eastereggs.flipacoin as flipACoin
import eastereggs.rockpaperscissors as RockPaperScissors
import eastereggs.rolladice as rollADice
import eastereggs.pickACard as pickACard
import eastereggs.pickanumber as pickANumber
import games.minesweeper as mineSweeper
import games.tictactoe as ticTacToe
import ScienceSimulators.physics.main as physics
import webservices.formservices as formservices
import games.hangman as hangman
import brain.chatbot as chatbot
import os

# This is the body of the program. This connects takes the answer, and then runs the command associated with the command.
globalPath = os.getcwd()
projectName = ''
inProject = False

def check(answer): 
	# Another exit checker
	if 'exit' in answer:
		return False
	elif 'good night' in answer:	
		return False
	else:
		return True

def processAnswer(mode, name, answer, lastCommand):
	global inProject
	global projectName
	answer = answer.lower()

	if answer == '' or answer == 'run last command':
		answer = lastCommand

	# Hello World example
	if answer == 'hello':
		textTesting(mode, 'hello')

	elif 'pick a card' in answer:
		pickACard.pickACard(mode)
	
	elif answer == 'chat':
		chatbot.chat(mode, name)

	# Prints options
	elif 'options' in answer: 
		system.options()
	
	# Exits program
	elif 'exit' in answer:
		textTesting(mode, 'Goodbye ' + name)

	elif 'good night' in answer:
		textTesting(mode, 'Good night ' + name)
		textTesting(mode, 'Get some sleep')

	# Sends email
	elif 'email' in answer:
		productivity.gmail()

	# Sets reminder
	elif 'reminder' in answer: 
		if mode == 'silent':
			productivity.reminderSilent(name)
		elif mode == 'production':
			productivity.reminderProduction(name)

	# prints the time 
	elif 'time' in answer and 'timer' not in answer: 
		if mode == 'silent':
			system.currentTimeSilent()
		elif mode == 'production':
			system.currentTimeProduction()

	# Flips a coin
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin(mode)

	elif 'stopwatch' in answer:
		system.stopwatch(mode)
	# Rolls a dice
	elif 'roll a dice' in answer: 
		rollADice.rolladice(mode)

	# Plays quick game of rock paper scissors 
	elif 'rock paper scissors' in answer:
		RockPaperScissors.rockpaperscissors(mode)

	# plays minesweeper
	elif 'minesweeper' in answer: 
		mineSweeper.minesweeper(mode)

	# Plays tic tac toe 
	elif 'tictactoe' in answer: 
		ticTacToe.ticTacToe(mode)
	# Plays Hangman
	elif 'hangman' in answer:
		hangman.hangman(mode)


	# Initializes a command line instance: Specific to silent mode, more of a development option
	elif 'command line' in answer:
		system.command_line()
	
	# Initializes a python line instance: Specific to silent mode, more of a development option
	elif 'python shell' in answer: 
		system.python_shell()
	
	# Runs my physics engine
	elif 'physics engine' in answer: 
		physics.run()
	
	#picks a number
	elif 'pick a number' in answer: 
		numbers = answer.replace('pick a number between', '')
		number1 = numbers.split(' and ')[0]
		number2 = numbers.split(' and ')[1]
		pickANumber.pickANumber(mode, number1, number2)
	# runs a simple ping request, returns results
	elif 'check network' in answer or 'network diagonostics' in answer:
		system.network_diagonistics()
	# runs a more in depth system diagonistic
	elif 'check system' in answer or 'system diagonostics' in answer:
		system.system_diagonistics()
	# runs all of my protocols, which are code that might not be convential
	elif 'run' in answer and 'protocol' in answer: 
		protocolone = answer.replace('run ', '')
		userProtocol = protocolone
		protocol.runProtocol(mode, userProtocol)
	# The start of my project interface, a place that I store other projects related to cliff (I.E. hardware)
	elif 'create project' in answer:
		projectName = answer.split()[2:]
		system.createProject(mode, ' '.join(projectName))
	# Allows C.L.I.F.F. to access the file system
	elif 'create file' in answer:
		answer = answer.replace('create file ', '')
		system.createFile(mode, answer)
	# Clears a file 
	elif 'clear file' in answer:
		answer = answer.replace('clear file ', '')
		system.clearFile(mode, answer)
	# 'Writes to a file'
	elif 'write to file' in answer:
		answer = answer.replace('write to file ', '')
		system.writeFile(mode, answer)
	# deletes a file
	elif 'delete file' in answer:
		answer = answer.replace('delete file ', '')
		confirm = input('Delete file {}? (Y/N) '.format(answer))
		confirm = confirm.lower()
		if confirm == 'y' or confirm == 'yes':
			try:
				os.remove(answer)	
			except FileNotFoundError:
				textTesting(mode, 'File does not exist')
			else:
				textTesting(mode, 'File Removed')	
	# allows cliff to fully autonomously run around the file system 
	elif 'change directory to' in answer:
		directory = answer.replace('change directory to ', '')
		if directory == '..':
			currentdirectory = os.getcwd().split('/')[:-1]
			os.chdir('/'.join(currentdirectory))
		else:
			os.chdir('{}/{}'.format(os.getcwd(), directory))
		textTesting(mode ,os.getcwd())
	# reads whats in a file
	elif 'read file' in answer:
		answer = answer.replace('read file ', '')
		system.readFile(mode, answer)
	# opens a project
	elif 'open project' in answer:
		project = answer.replace('open project ', '')
		inProject = True
		projectName = project
		system.openProject(mode, project)
	# runs a command for the bash terminal
	elif 'run command' in answer:
		command = answer.replace('run command ', '')
		os.system(command)
	# closes out of a project
	elif 'close project' in answer:
		system.closeProject(mode)
		inProject = False
	# opens my notes
	elif 'open' in answer and 'notes' in answer:
		note = answer.replace('open ', '')
		note = note.replace('notes ', '')
		system.openNote(mode, '/home/connor/CLIFF/CLIFF/journals/notes/{}'.format(note))
	# creates a note
	elif 'create' in answer and 'note' in answer: 
		system.createNote(mode)

	elif 'list notes' in answer:
		system.listNotes(mode)

	elif 'delete note' in answer:
		note = answer.replace('delete note ', '')
		system.deleteNote(mode, note)

	elif 'run timer for ' in answer:
		time = answer.replace('run timer for ', '')
		system.timer(mode, time)

	else: 
		textTesting(mode, 'I\'m sorry, we don\'t appear to have the command ' + answer)
	if inProject == False:
		lastCommand = answer
		return lastCommand, inProject, ''
	else:
		lastCommand = answer
		return lastCommand, inProject, projectName

def processAnswerWebSite(name, answer):

	answer = answer.lower()

	# Hello World example
	if answer == 'hello':
		return 'hello'

	if answer == 'test':
		formservices.GetWebInput('command', 'Test')

	# Exits program
	elif 'exit' in answer:
		return 'Goodbye ' + name

	# prints the time 
	elif 'time' in answer: 
		time = system.currentTimeWebsite()
		return time

	else: 
		return 'I\'m sorry, we don\'t appear to have the command ' + answer
