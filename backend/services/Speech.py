from gtts import gTTS 
import os 
import speech_recognition as sr
import time

# converts text to speech using gtts module
def textToSpeech(mytext):
    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine,  
    # marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False, ) 
  
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("soundfile.mp3") 
  
    # Playing the converted file 
    os.system("mpg321 soundfile.mp3")
# converts speech to text using speech_recognition
def speechToText(): 
    r = sr.Recognizer()
    print("mic drop ready?")
    time.sleep(1)
    mic = sr.Microphone()
    print("mic drop detected")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        test = 1
        while test == 1:
            try:
                audio = r.listen(source)
                question = r.recognize_google(audio)
                test = 2
            except sr.UnknownValueError:
             #   textToSpeech('Sorry, I didn\'t catch that')
                 print("Unrecognizable Speech")
        if "cliff" in question:
       	    return question
        else:
            speechToText()
# modular code to prevent more reduncancy than neccassary, checks mode to see whether it should 
# print to the console or speak it using computers 
def textTesting(mode, text):
    if mode == 'production':
        textToSpeech(text)

    elif mode == 'silent':
        print(text)

# modular code to prevent more reduncancy than neccassary, checks mode to see whether it should 
# check for input from a microphone, or accept keyboard input 
def inputTesting(mode, text):
    if mode == 'production':
        textToSpeech(text)
        answer = speechToText()
        return answer
    elif mode == 'silent':
        answer = input(text)
        return answer
