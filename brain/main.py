
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
        self.binarySignal = 1

    # connects with another nueron, "pinging" it with a signal
    def connect(self, id):
        name = self.name
        if id == 1:
            self.connection1.sendConnectSignal(name)
        if id == 2:
            self.connection2.sendConnectSignal(name)
        if id == 3: 
            self.connection3.sendConnectSignal(name)

    # sends data back when pinged. A single binary off or on signal
    def sendData(self, id):
        return(self.binarySignal)
    
    # The ping class. Gets pinged, sends data back to the neuron that pinged it
    def sendConnectSignal(self, name):
        self.sendData(id)
        return 'connected'

    def getConnectionIDByName(self, name):
        id = self.connectionNames[name]
        return id

node1 = node('node1')
node2 = node('node2')
node3 = node('node3')
node4 = node('node4')

node1.setConnections(node2, node3, node4)
node2.setConnections(node1, node3, node4)
node3.setConnections(node1, node2, node4)
node4.setConnections(node1, node2, node3)

hello = node1.connect(3)

