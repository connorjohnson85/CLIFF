alphabet = "abcdefghijklmnopqrstuvwxyz"

def ceaserCipher(message, shifts, encrypt):
	if encrypt == True:
		newMessage = ""
		for letter in message:
			letterPosition = alphabet.find(message)
			try: 
				newMessage += alphabet[letterPosition + shifts]
			except:
				newIndex = -(alphabet.length - letterPosition)
