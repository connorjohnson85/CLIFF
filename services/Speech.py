from gtts import gTTS 
import os 
import speech_recognition as sr

  
def textToSpeech(mytext):
  
# Language in which you want to convert 
    language = 'en'
  
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
  
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("welcome.mp3") 
  
    # Playing the converted file 
    os.system("mpg321 welcome.mp3")

def speechToText(): 
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        question = r.recognize_google(audio)
    return question

def textTesting(mode, text):
    if mode == 'production':
        textToSpeech(text)
    elif mode == 'silent':
        print(text)

def inputTesting(mode, text):
    if mode == 'production':
        textToSpeech(text)
        answer = speechToText()
        return answer
    elif mode == 'silent':
        answer = input(text)
        return answer