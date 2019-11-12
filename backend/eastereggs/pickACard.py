import random
from services.Speech import textTesting as TTS

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

def pickACard(mode):
    card = random.choice(cards)
    suit = random.choice(suits)
    TTS(mode, 'Your card is a {0} of {1}'.format(card, suit))
