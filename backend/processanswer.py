import backend.commands.mymath as mymath
import backend.commands.system as system
import backend.commands.productivity as productivity
from backend.services.Speech import textToSpeech as textToSpeech
import backend.eastereggs.flipacoin as flipACoin
import backend.eastereggs.rockpaperscissors as RockPaperScissors
import backend.eastereggs.rolladice as rollADice
import backend.games.minesweeper as mineSweeper
import backend.games.tictactoe as ticTacToe
import backend.ScienceSimulators.physics.main as physics

# This is the body of the program. This connects takes the answer, and then runs the command associated with the command. When it gets too large, I May have to create a new approach to this

def processAnswerProduction(name, answer): 
	
	answer = answer.lower()
	
	# Hello world test
	if answer == 'hello':
		textToSpeech('hello')

	# Prints options
	elif 'options' in answer: 
		system.options()
	
	#Exits 
	elif 'exit' in answer:
		textToSpeech('Goodbye ' + name)

	# Sends email
	elif 'email' in answer:
		productivity.gmail()

	# Set Reminder
	elif 'reminder' in answer: 
		productivity.reminderSilent(name)

	# Prints time
	elif 'what\'s the time' in answer: 
		system.currentTimeProduction()
	
	# Flips a coin
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin('production')

	# Rolls a dice
	elif 'roll a dice' in answer: 
		rollADice.rolladice('production')
	
	# Plays a quick game of rock paper scissors 
	elif 'rock paper scissors' in answer:
		RockPaperScissors.rockpaperscissors('production')

	# Runs minesweeper
	elif 'minesweeper' in answer: 
		mineSweeper.minesweeper('production')

	# Runs tic tac toe
	elif 'tic tac toe' in answer: 
		ticTacToe.ticTacToe('production')
	
	# Runs my physics engine 
	elif 'physics engine' in answer: 
		physics.run()
	
	else: 
		textToSpeech('I\'m sorry, we don\'t appear to have the command ' + answer)

def processAnswerSilent(name, answer):

	answer = answer.lower()

	# Hello World example
	if answer == 'hello':
		print('hello')

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
		productivity.reminderSilent(name)

	# prints the time 
	elif 'time' in answer: 
		system.currentTimeSilent()

	# Flips a coin
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin('silent')

	# Rolls a dice
	elif 'roll a dice' in answer: 
		rollADice.rolladice('silent')

	# Plays quick game of rock paper scissors 
	elif 'rock paper scissors' in answer:
		RockPaperScissors.rockpaperscissors('silent')

	# plays minesweeper
	elif 'minesweeper' in answer: 
		mineSweeper.minesweeper('silent')

	# Plays tic tac toe 
	elif 'tictactoe' in answer: 
		ticTacToe.ticTacToe('silent')

	# Initializes a command line instance: Specific to silent mode, more of a development option
	elif 'command line' in answer:
		system.command_line()
	
	# Initializes a python line instance: Specific to silent mode, more of a development option
	elif 'python shell' in answer: 
		system.python_shell
	
	# Runs my physics engine
	elif 'physics engine' in answer: 
		physics.run()

	else: 
		print('I\'m sorry, we don\'t appear to have the command ' + answer)

def check(answer): 
	# Another exit checker
	if answer == 'exit':
		return False
	else:
		return True

def processAnswerWebSite(name, answer):

	answer = answer.lower()

	# Hello World example
	if answer == 'hello':
		return 'hello'

	# Exits program
	elif 'exit' in answer:
		return 'Goodbye ' + name

	# prints the time 
	elif 'time' in answer: 
		time = system.currentTimeWebsite()
		return time

	else: 
		return 'I\'m sorry, we don\'t appear to have the command ' + answer