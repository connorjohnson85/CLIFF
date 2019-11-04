import math

def equation1(finalVelocity, initialVelocity, acceleration, time):
    if acceleration == False:
        acceleration = (finalVelocity - initialVelocity)/time
        return acceleration
    if finalVelocity == False:
        finalVelocity = initialVelocity + acceleration*time
        return finalVelocity
    if initialVelocity == False: 
        initialVelocity = finalVelocity - acceleration*time
        return initialVelocity
    if time == False:
        time = (finalVelocity - initialVelocity)/acceleration
        return time 

def equation2(finalPosition, startPosition, initialVelocity, time, accelaration):
    if finalPosition == False:
        finalPosition = startPosition + initialVelocity*time + .5*accelaration*(time**2)
        return finalPosition
    if startPosition == False:
        startPosition = finalPosition - initialVelocity*time + .5*accelaration*(time**2)
        return startPosition
    if initalVelocity == False: 
        initalVelocity = (finalPosition-startPosition-.5*accelaration*(time**2))/time
        return initalVelocity
    if accelaration == False: 
        accelaration = (2*(finalPosition-startPosition-initalVelocity*time))/(time**2)
        return accelaration
    if time == False:
        time = math.sqrt(2*(finalPosition-startPosition-initalVelocity)/accelaration)
        return time
def equation3(finalVelocity, initialVelocity, accelaration, finalPosition, startPosition):
    
    print(finalVelocity, initialVelocity, accelaration, finalPosition, startPosition)

