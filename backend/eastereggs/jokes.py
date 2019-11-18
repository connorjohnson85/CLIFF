import services.Speech.TextTesting as TextTesting
import random

jokelist = ['hello', 'Dude']
punchlines = ['Knock knock', 'dude']

def jokes(mode):
    joke = random.choice(jokelist)
    TextTesting(joke)
    jokeIndex = jokelist.index(joke)
    TextTesting(punchlines[jokeIndex])

