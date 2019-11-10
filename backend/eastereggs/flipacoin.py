import random
from services.Speech import textToSpeech as ts

# Easter Egg. Flips a coin
def flipacoin(mode):
    # Picks random side
    side = random.choice(['Heads', 'Tails'])
    # Differentiates between modes
    if mode == 'silent':
        print(side)
    if mode == 'production':
        ts(side)