import processanswer as p
from services.Speech import textToSpeech as ts
from services.Speech import speechToText as speechrecognition

def run(name, mode): 
    AIOn = True
    if mode == 'production':
        while AIOn == True: 
            ts('What do you need assistance with today?')
            question = speechrecognition()
         
            AIOn = p.check(question)
            p.processAnswerProduction(name, question)
    if mode == 'silent': 
         while AIOn == True: 
            print('What do you need assistance with today?')
            question = input(name + ': ')
            AIOn = p.check(question)
            p.processAnswerSilent(name, question)