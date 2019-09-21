import commands.mymath as mymath
import commands.system as system
import commands.productivity as productivity
from services.Speech import textToSpeech as textToSpeech
import eastereggs.flipacoin as flipACoin
import eastereggs.rockpaperscissors as RockPaperScissors
import eastereggs.rolladice as rollADice
import games.minesweeper as mineSweeper
import games.tictactoe as ticTacToe
import ScienceSimulators.physics.main as physics

def processAnswerProduction(name, answer): 
	answer = answer.lower()
	if answer == 'hello':
		textToSpeech('hello')
	elif 'options' in answer: 
		system.options()
	elif 'exit' in answer:
		textToSpeech('Goodbye ' + name)
	elif 'email' in answer:
		productivity.gmail()
	elif 'reminder' in answer: 
		productivity.reminderSilent(name)
	elif 'what\'s the time' in answer: 
		system.currentTimeProduction()
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin('production')
	elif 'roll a dice' in answer: 
		rollADice.rolladice('production')
	elif 'rock paper scissors' in answer:
		RockPaperScissors.rockpaperscissors('production')
	elif 'minesweeper' in answer: 
		mineSweeper.minesweeper('production')
	elif 'tictactoe' in answer: 
		ticTacToe.ticTacToe('production')
	elif 'physics engine' in answer: 
		physics.run()
	else: 
		textToSpeech('I\'m sorry, we don\'t appear to have the command ' + answer)

def processAnswerSilent(name, answer):
	answer = answer.lower()
	if answer == 'hello':
		print('hello')
	elif 'options' in answer: 
		system.options()
	elif 'exit' in answer:
		print('Goodbye ' + name)
	elif 'email' in answer:
		productivity.gmail()
	elif 'reminder' in answer: 
		productivity.reminderSilent(name)
	elif 'what\'s the time' in answer: 
		system.currentTimeSilent()
	elif 'flip a coin' in answer: 
		flipACoin.flipacoin('silent')
	elif 'roll a dice' in answer: 
		rollADice.rolladice('silent')
	elif 'rock paper scissors' in answer:
		RockPaperScissors.rockpaperscissors('silent')
	elif 'minesweeper' in answer: 
		mineSweeper.minesweeper('silent')
	elif 'tictactoe' in answer: 
		ticTacToe.ticTacToe('silent')
	elif 'command line' in answer:
		system.command_line()
	elif 'python shell' in answer: 
		system.python_shell
	elif 'physics engine' in answer: 
		physics.run()
	else: 
		print('I\'m sorry, we don\'t appear to have the command ' + answer)

def check(answer): 
	if answer == 'exit':
		return False
	else:
		return True