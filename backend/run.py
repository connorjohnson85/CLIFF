import backend.processanswer as p
from backend.services.Speech import textToSpeech as ts
from backend.services.Speech import speechToText as speechrecognition

# Puts it all in a while loop to take infinite answers
def run(name, mode): 
    AIOn = True
    if mode == 'production':
        while AIOn == True: 
            ts('What do you need assistance with today?')
            # Runs speech Recognition
            question = speechrecognition()
            AIOn = p.check(question)
            p.processAnswerProduction(name, question)
    if mode == 'silent': 
         while AIOn == True: 
            print('What do you need assistance with today?')
            question = input(name + ': ')
            AIOn = p.check(question)
            p.processAnswerSilent(name, question)