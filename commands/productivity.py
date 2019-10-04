import json
from services.Speech import textToSpeech as ts


def gmail():
    import smtplib, ssl

    port = 465  # For SSL
    password = '@The-serum101?!'

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("connorjohnson853@gmail.com", password)
        print('sending email')

def reminderSilent(name): 
        print('C.L.I.F.F: When would you like me to set a reminder?')
        time = input(name + ': ')
        print('C.L.I.F.F: What would you like it to say?')
        body = input(name + ': ')
        print('C.L.I.F.F: I have a reminder set at ' + time + ' To ' + body + '. Is that correct?')
        correction = input('(y/n): ')
        if correction == 'y': 
                print('Setting Reminder')
        else: 
                print('Ok')

def reminderProduction(name):
        ts('When would you like me to set a remdinder?')
        time = input(name + ': ')
        ts('C.L.I.F.F: What would you like it to say?')
        body = input(name + ': ')
        ts('C.L.I.F.F: I have a reminder set at ' + time + ' To ' + body + '. Is that correct?')
        correction = input('(y/n): ')
        if correction == 'y': 
                ts('Setting Reminder')
        else: 
                ts('Ok')