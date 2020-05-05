import random
def hangman(mode):
	# initializises a template of blank words to pick from
	words = ['template', "word", 'python', 'cyberspace', 'support', 'total', 'random', 'hymn',
'love', 'easy', 'cheese', 'maximus', 'xylophone', 'game', 'good', 'powerful', 'unstoppable', 
'phase', 'medicated', 'thoughts', 'strengths', 'quantum', 'nanotechnology', 
'friend', 'zoned']

	secretWord = random.choice(words)
	dashes = ''
	for letter in secretWord:
	    dashes += '-'

	guesses_left = 10
	alreadyBeenGuessed = ''

	while guesses_left > 0:
		guess = ''
		while True:
			guess = input("guess a letter: ")
			guess = guess.lower()
			if guess not in alreadyBeenGuessed and len(guess) == 1:
				alreadyBeenGuessed += guess
				break
			elif guess in alreadyBeenGuessed:
				print('You\'ve already guessed that letter!')
			else:
				print('Must be a single lowercase letter')
		if guess in secretWord:
			dashes, oldDashes = '', dashes
			for item in secretWord:
				if guess == item:
					dashes += guess
				else: 
					dashes += oldDashes[secretWord.find(item)]
		else:
			print('{} is not in the word!'.format(guess))
			guesses_left -= 1
	
		if secretWord == dashes:
			print('You win! Good Job! The word was: {}'.format(secretWord))
			break
		elif guesses_left <= 0:
			print('You lost! The word was: {}'.format(secretWord))
			break
		else:
			print('You have {} guesses left'.format(guesses_left)) 
			print(dashes)
		


