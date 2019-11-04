import random

# my nueron model class. Expect it to change. A lot XD XD XD
class node():
    # initializes a "nueron" with just a name
    def __init__(self, name):
        self.name = name
    
    # initializes a connection with three other nuerons. a simple network, not designed for much complexity
    def setConnections(self, connection1, connection2, connection3):
        self.connection1 = connection1
        self.connection2 = connection2
        self.connection3 = connection3
        self.connectionNames = {
            connection1.name: 1,
            connection2.name: 2,
            connection3.name: 3
            } 
        self.binarySignal = 0

    # connects with another nueron, "pinging" it with a signal
    def connect(self, id):
        name = self.name
        if id == 1:
            response = self.connection1.sendConnectSignal(name)
        if id == 2:
            response = self.connection2.sendConnectSignal(name)
        if id == 3: 
            response = self.connection3.sendConnectSignal(name)
        return response

    # sends data back when pinged. A single binary off or on signal
    def sendData(self, id):
        if id == 1:
            response = self.connection1.receiveData(self.name, self.binarySignal)
        if id == 2:
            response = self.connection2.receiveData(self.name, self.binarySignal)
        if id == 3:
            response = self.connection3.receiveData(self.name, self.binarySignal)
        return response 
    # The ping class. Gets pinged, sends data back to the neuron that pinged it
    def sendConnectSignal(self, name):
        response = self.sendData(self.getConnectionIDByName(name))
        return response
    def receiveData(self, name, data):
        return name, data


    def getConnectionIDByName(self, name):
        id = self.connectionNames[name]
        return id

class nodeCluster():
    
    def __init__(self, name):
        self.name = name 

class brain():
    def __init__(self, name):
        self.name = name

node1 = node('node1')
node2 = node('node2')
node3 = node('node3')
node4 = node('node4')

node1.setConnections(node2, node3, node4)
node2.setConnections(node1, node3, node4)
node3.setConnections(node1, node2, node4)
node4.setConnections(node1, node2, node3)

response = node1.connect(1)
x = 0
while x != 1000:
    response = node1.connect(random.randint(1,3))
    if response[1] == 0:
        node1.binarySignal = 1
        if response[0] == 'node2':
            node2.binarySignal = 1
        if response[0] == 'node3':
            node3.binarySignal = 1
        if response[0] == 'node4':
            node4.binarySignal = 1
    else:
        node1.binarySignal = 0
        if response[0] == 'node2':
            node2.binarySignal = 0
        if response[0] == 'node3':
            node3.binarySignal = 0
        if response[0] == 'node4':
            node4.binarySignal = 0
    x += 1 

print(node1.binarySignal)
print(node2.binarySignal)
print(node3.binarySignal)
print(node4.binarySignal)