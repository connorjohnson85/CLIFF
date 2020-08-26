import random
import math
import pyaudio
from services.Speech import textTesting, inputTesting
from commands.otherProtocols.protocols.protocolzero import protocolZero 

def testProtocol(mode):
    textTesting(mode, 'Protocols working as expected sir')

def listProtocols(mode):
    for item in protocols:
        textTesting(mode, item)

def protocol1(mode):
	print("Running protocol one... ")

def protocol2(mode):
	print("Running protocol two... ")

def protocol3(mode):
	path = "/home/connor/CLIFF/CLIFF/backend/music"
	

protocols = {'test protocol': testProtocol, 'list protocols': listProtocols, "protocol one": protocol1, "protocol two": protocol2, "protocol3": protocol3, 
'protocol zero': protocolZero}

def runProtocol(mode, protocol):
    try: 
        function=protocols[protocol]
        function(mode)
    except KeyError:
        print('{0} not found'.format(protocol))
