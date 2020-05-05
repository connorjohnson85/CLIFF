logFile = open('hardware/project Iron Man/ArcReactor/log.txt', 'a+')

def checkReactorFuelLevels():
    logFile.write('Fuel Levels at 54%')

def reactorCoreCheck():
    logFile.write('Reactor integretity at 100%')

def energyUsage():
    logFile.write('We are currently using 75% \of the current energy levels')

def ALL():
    return '''Fuel Levels at 54%
Reactor integretity at 100%
We are currently using 75% of the current energy levels
'''