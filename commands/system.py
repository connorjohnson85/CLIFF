
import datetime
from services.Speech import textToSpeech as ts

def options():
    print('C.L.I.F.F: I can currently recognize speech!')

def currentTimeSilent():
    print(datetime.datetime.now().date(), datetime.datetime.now().time())
def currentTimeProduction():
    ts('The current time is: ' + datetime.datetime.now().date() + ' ' + datetime.datetime.now().time())