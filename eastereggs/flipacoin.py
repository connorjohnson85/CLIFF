import random
from services.Speech import textToSpeech as ts


def flipacoin(mode):
    side = random.choice(['Heads', 'Tails'])
    if mode == 'silent':
        print(side)
    if mode == 'production':
        ts(side)