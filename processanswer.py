import commands.mymath as mymath
import commands.system as system
import commands.productivity as productivity
from services.Speech import textToSpeech as ts
import eastereggs.flipacoin as fac
import eastereggs.rockpaperscissors as rps
import eastereggs.rolladice as rad

def processAnswerProduction(name, answer): 
	if answer == 'hello':
		ts('hello')
	elif 'options' in answer: 
		system.options()
	elif 'exit' in answer:
		ts('Goodbye ' + name)
	elif 'email' in answer:
		productivity.gmail()
	elif 'reminder' in answer: 
		productivity.reminderSilent(name)
	elif 'what\'s the time' in answer: 
		system.currentTimeProduction()
	elif 'flip a coin' in answer: 
		fac.flipacoin('production')
	elif 'roll a dice' in answer: 
		rad.rolladice('production')
	elif 'rock paper scissors' in answer:
		rps.rockpaperscissors('production')
	else: 
		ts('I\'m sorry, we don\'t appear to have the command ' + answer)

def processAnswerSilent(name, answer):
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
		fac.flipacoin('silent')
	elif 'roll a dice' in answer: 
		rad.rolladice('silent')
	elif 'rock paper scissors' in answer:
		rps.rockpaperscissors('silent')
	else: 
		print('I\'m sorry, we don\'t appear to have the command ' + answer)

def check(answer): 
	if answer == 'exit':
		return False
	else:
		return True