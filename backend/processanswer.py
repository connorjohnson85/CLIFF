import commands.mymath as mymath
import commands.system as system
import commands.productivity as productivity
import commands.protocols as protocol
from services.Speech import textToSpeech as textToSpeech
import eastereggs.flipacoin as flipACoin
import eastereggs.rockpaperscissors as RockPaperScissors
import eastereggs.rolladice as rollADice
import games.minesweeper as mineSweeper
import games.tictactoe as ticTacToe
import ScienceSimulators.physics.main as physics
import webservices.formservices as formservices
import eastereggs.pickACard as pickACard
from services.Speech import textTesting
from services.Speech import inputTesting
import eastereggs.pickanumber as pickANumber
# This is the body of the program. This connects takes the answer, and then runs the command associated with the command. When it gets too large, I May have to create a new approach to this

def check(answer): 
	# Another exit checker
	if answer == 'exit':
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
		print('Goodbye ' + name)

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
		system.python_shell
	
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

	else: 
		print('I\'m sorry, we don\'t appear to have the command ' + answer)

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