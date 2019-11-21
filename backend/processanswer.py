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
import os

# This is the body of the program. This connects takes the answer, and then runs the command associated with the command. When it gets too large, I May have to create a new approach to this

def check(answer): 
	# Another exit checker
	if 'exit' in answer:
		return False
	elif 'good night' in answer:	
		return False
	else:
		return True

def processAnswer(mode, name, answer):

	answer = answer.lower()

	# Hello World example
	if answer == 'hello':
		textTesting(mode, 'hello')

	elif 'pick a card' in answer:
		pickACard.pickACard(mode)

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
	elif 'time' in answer: 
		if mode == 'silent':
			system.currentTimeSilent()
		elif mode == 'production':
			system.currentTimeProduction()

	# Flips a coin
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin(mode)

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

	# Initializes a command line instance: Specific to silent mode, more of a development option
	elif 'command line' in answer:
		system.command_line()
	
	# Initializes a python line instance: Specific to silent mode, more of a development option
	elif 'python shell' in answer: 
		system.python_shell()
	
	# Runs my physics engine
	elif 'physics engine' in answer: 
		physics.run()

	elif 'pick a number' in answer: 
		pickANumber.pickANumber(mode)

	elif 'check network' in answer or 'network diagonostics' in answer:
		system.network_diagonistics()

	elif 'check system' in answer or 'system diagonostics' in answer:
		system.system_diagonistics()

	elif 'run' in answer and 'protocol' in answer: 
		answer = answer.replace('run ', '')
		userProtocol = answer
		protocol.runProtocol(mode, userProtocol)

	elif 'create project' in answer:
		projectName = answer.split()[2:]
		system.createProject(' '.join(projectName))

	elif 'create file' in answer:
		answer = answer.replace('create file ', '')
		system.createFile(mode, answer)
	
	elif 'clear file' in answer:
		answer = answer.replace('clear file ', '')
		system.clearFile(mode, answer)

	elif 'write to file' in answer:
		answer = answer.replace('write to file ', '')
		system.writeFile(mode, answer)

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

	elif 'change directory to' in answer:
		directory = answer.replace('change directory to ', '')
		if directory == '..':
			currentdirectory = os.getcwd().split('/')[:-1]
			os.chdir('/'.join(currentdirectory))
		else:
			os.chdir('{}/{}'.format(os.getcwd(), directory))
		textTesting(mode ,os.getcwd())

	elif 'read file' in answer:
		answer = answer.replace('read file ', '')
		system.readFile(mode, answer)

	elif 'open project' in answer:
		project = answer.replace('open project ', '')
		system.openProject(mode, project)

	elif 'run command' in answer:
		command = answer.replace('run command ', '')
		os.system(command)

	else: 
		textTesting(mode, 'I\'m sorry, we don\'t appear to have the command ' + answer)

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