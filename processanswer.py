import commands.mymath as mymath
import commands.system as system
import commands.productivity as productivity
from services.Speech import textToSpeech as ts

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
	else: 
		print('I\'m sorry, we don\'t appear to have the command ' + answer)

def check(answer): 
	if answer == 'exit':
		return False
	else:
		return True