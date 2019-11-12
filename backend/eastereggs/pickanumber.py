import random
from services.Speech import inputTesting, textTesting

def pickANumber(mode):
    start = inputTesting(mode, 'First number? ')
    end = inputTesting(mode, 'Second number? ')
    number = random.randint(int(start), int(end))
    textTesting(mode, 'picking a number between {0} and {1}'.format(start, end))
    textTesting(mode, 'Your number is {0}'.format(number))

