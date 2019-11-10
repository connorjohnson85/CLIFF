from flask import flash, url_for, redirect

def GetWebInput(url, inputString):
    flash(inputString)
    redirect(url_for(url))
    
