import random
batman = not 'batman'
print(batman)
# my nueron model class. Expect it to change. A lot XD XD XD
class node():
    # initializes a "nueron" with just a name
    def __init__(self, name):
        self.name = name
        self.binarySignal = 0
    
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

    def setConnections(self, connection1, connection2, connection3, connection4):
        self.connection1 = connection1
        self.connection2 = connection2
        self.connection3 = connection3
        self.connection4 = connection4

    def setChildren(self, child1, child2, child3, child4):
        self.child1 = child1
        self.child2 = child2
        self.child3 = child3
        self.child4 = child4
    
    def readChildren(self):
        print(self.child1.binarySignal)
        print(self.child2.binarySignal)
        print(self.child3.binarySignal)
        print(self.child4.binarySignal)
        return self.child1.binarySignal, self.child2.binarySignal, self.child3.binarySignal, self.child4.binarySignal

class brain():
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def setConnections(self, connections):
        self.connection1 = connection1
        self.connection2 = connection2
        self.connection3 = connection3
        self.connection4 = connection4
        self.connection5 = connection5
    
    def setChildren(self, children):
        childs = []
        for item in children:
            childs.append(item)
        self.children = childs
    
    def readChildren(self):
        values = []
        for item in self.children:
            print(item.name)
            response = item.readChildren()
            values.append(response)
        return(values)
        
    def __repr__(self):
        return('name: {0} purpose: {1}'.format(self.name, self.purpose))



node1 = node('node1')
node2 = node('node2')a cq   1
node3 = node('node3')
node4 = node('node4')
node5 = node('node5')
node6 = node('node6') 
node7 = node('node7')
node8 = node('node8')
node9 = node('node9')
node10 = node('node10')
node11 = node('node11')
node12 = node('node12')
node13 = node('node13')
node14 = node('node14')
node15 = node('node15')
node16 = node('node16')
node17 = node('node17')
node18 = node('node18')
node19 = node('node19')
node20 = node('node20')

node1.setConnections(node2, node3, node4)
node2.setConnections(node1, node3, node4)
node3.setConnections(node1, node2, node4)
node4.setConnections(node1, node2, node3)

nodeCluster1 = nodeCluster('nodecluster1')
nodeCluster2 = nodeCluster('nodecluster2')
nodeCluster3 = nodeCluster('nodecluster3')
nodeCluster4 = nodeCluster('nodecluster4')
nodeCluster5 = nodeCluster('nodecluster5')

nodeCluster1.setChildren(node1, node2, node3, node4)
nodeCluster2.setChildren(node5, node6, node7, node8)
nodeCluster3.setChildren(node9, node10, node11, node12)
nodeCluster4.setChildren(node13, node14, node15, node16)
nodeCluster5.setChildren(node17, node18, node19, node20)

nodeCluster1.setConnections(nodeCluster2, nodeCluster3, nodeCluster4, nodeCluster5)
nodeCluster2.setConnections(nodeCluster1, nodeCluster3, nodeCluster4, nodeCluster5)
nodeCluster3.setConnections(nodeCluster1, nodeCluster2, nodeCluster4, nodeCluster5)
nodeCluster4.setConnections(nodeCluster1, nodeCluster2, nodeCluster3, nodeCluster5)
nodeCluster1.setConnections(nodeCluster1, nodeCluster2, nodeCluster3, nodeCluster4)

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

nodeCluster1.readChildren()

brain1 = brain('brain1', 'Math')

brain1.setChildren([nodeCluster1, nodeCluster2, nodeCluster3, nodeCluster4, nodeCluster5])

response = brain1.readChildren()

print(response)

