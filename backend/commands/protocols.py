import random
import math
from services.Speech import textTesting, inputTesting

def testProtocol(mode):
    textTesting(mode, 'Protocols working as expected sir')

def listProtocols(mode):
    for item in protocols:
        textTesting(mode, item)


protocols = {'test protocol': testProtocol, 'list protocols': listProtocols}

def runProtocol(mode, protocol):
    try: 
        function=protocols[protocol]
        function(mode)
    except KeyError:
        print('{0} not found'.format(protocol))
