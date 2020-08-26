alphabet = "aZbYcXdWeVfUgThSiRjQkPlOmNnMoLpKqJrIsHtGuFvEwDxCyBzA"

def ceaserCipher(message, shifts, encrypt):
	if encrypt == True:
		newMessage = ""
		for letter in message:
			letterPosition = alphabet.find(letter)
			try:
				newMessage += alphabet[letterPosition + shifts]
			except:
				newIndex = (len(alphabet) - letterPosition)
				newMessage += alphabet[newIndex]
		return newMessage

	else:
		newMessage = ""
		for letter in message:
			letterPosition = alphabet.find(letter)
			try:
				newMessage += alphabet[letterPosition - shifts]
			except:
				newIndex = -len(alphabet) + shifts
				newMessage += alphabet[newIndex]
		return newMessage
nope = ceaserCipher("hello", 36, True)
print(nope)
print(ceaserCipher(nope, 36, False))
