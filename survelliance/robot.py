from pynput.keybaord import Key, Listener

def on_press(key): 
    print('{0} pressed'.format(key))
def on_release(key):
    print('{0} pressed'.format(key))
    if key == Key.esc:
        return False

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()




def connectToRover():
    print('Filler till I finish rover, connect it to cliff')

def move():
    #Todo: Get keyinputs, control rover, move it, get camera inpout, give rover things to do
    rover = True 
    while rover == True:
        if keyPressed == "Space":
            rover == False
        elif keyPressed == "Right Arrow":
            turn = "Right"
            direction = "None"
        elif keyPressed == "Left Arrow":
            turn = "Left"
            direction = "None"
        elif keyPressed == "Up Arrow":
            turn = "None"
            directon = "Forward"
        elif keyPressed == "Down Arrow":
            turn = "None"
            direction = "Backward"
        else:
            turn = "None"
            direction = "None"