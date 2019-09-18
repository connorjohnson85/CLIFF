# text based only
from services.Speech import textTesting, textToSpeech, speechToText, inputTesting 

def minesweeper(mode): 
    difficulty = inputTesting(mode, 'Easy, medium, or hard?')
    length = inputTesting(mode, 'Small, Medium, or Large?')
    textTesting(mode, length + difficulty)
    
minesweeper('silent')