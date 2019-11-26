import processanswer as p
from services.Speech import textToSpeech as ts
from services.Speech import speechToText as speechrecognition

# Puts it all in a while loop to take infinite answers
def run(name, mode): 
    AIOn = True
    if mode == 'production':
        ts('What do you need assistance with today?')

        while AIOn == True: 
            # Runs speech Recognition
            question = speechrecognition()
            AIOn = p.check(question)
            p.processAnswer(mode, name, question)
            ts('command ran')

    if mode == 'silent':  
        print('What do you need assistance with today?')

        while AIOn == True:
            question = input(name + ': ')
            AIOn = p.check(question)
            p.processAnswer(mode, name, question)
            print('command ran successfully')

