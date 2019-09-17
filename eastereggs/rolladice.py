import random
from services.Speech import textToSpeech as ts

def rolladice(mode):
    if mode == 'production':
        ts('rolling...')
        ts('your number is: ' + str(random.randint(1, 6)))
    if mode == 'silent':
        print('rolling...')
        print('your number is: ' + str(random.randint(1, 6)))