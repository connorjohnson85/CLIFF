import json
from services.Speech import textToSpeech as ts
import smtplib

#
# All productivity type functions are stored here: I.E. Notes, reminders, and sending gmail
#

# Sends Gmail
def gmail():

        # Python code to illustrate Sending mail from  
        # your Gmail account  
        
  
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
  
        # start TLS for security 
        s.starttls() 
        # Authentication 
        s.login("connorjohnson853@gmail.com", "@The-serum101?!") 
  
        # message to be sent 
        message = input('Body Paragraph')
  
        # sending the mail 
        s.sendmail("connorjohnson853@gmail.com", "abbeymjones9@gmail.com", message) 
  
        # terminating the session 
        s.quit() 

# Sets Reminder TODO: SET REMINDER ;) 
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

