import backend.ScienceSimulators.chemistry.periodicTable as elements

element = elements.periodicTable()

class particleAccelarator():
    def __init__(self):
        self.elements = []

    def on(self):
        self.on = True

    def off(self):
        self.on = False 

    def add(self, elementName):
        self.elements.append(Element)
        print(self.elements)

dude = particleAccelarator()
dude.on()
