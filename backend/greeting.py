from services.Speech import textToSpeech as ts

# Greeting functions defined to be used more effiecently, gets name of current user

def greetproduction(): 
	ts('Welcome back sir') 
	name = 'Connor'
	return(name)

def greetsilent():
	print('C.L.I.F.F: Welcome back sir')
	name = 'Connor'
	return name

def greettest():
	print('C.L.I.F.F: Hello! I am Cliff! What is your name?')
	name = input('Blank: ')
	print('C.L.I.F.F: Hi ' + name + '!')
	return name