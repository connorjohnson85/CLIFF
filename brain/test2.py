import math

class Brain():
    def __init__(self, numOfNodes, neighborNumber):
        self.k = neighborNumber
        self.numOfNodes = numOfNodes
        self.nodes = []
        for item in range(0, numOfNodes):
            print(item)
            newNode = Node('node {0}'.format(item+1), item+1)
            self.nodes.append(newNode)
        for item in self.nodes:
            connections = []
            for num in range(0, neighborNumber):
                if self.nodes[item.num].num - neighborNumber > 0 and self.nodes[item.num].num + neighborNumber <= numOfNodes:
                    connections.append(self.nodes[item.num+num])
                    connections.append(self.nodes[item.num-num])
                elif self.nodes[item.num].num - neighborNumber < 0:
                    connections.append(self.nodes[item.num-num])
                elif self.nodes[item.num].num + neighborNumber > numOfNodes:
                    connections.append(self.nodes[item.num-num])
            item.setConnections(connections)

class Node():
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.binarySignal = 0

    def setConnections(self, connections):
        self.connections = []
        for item in connections: 
            self.connections.append(item)

    def __repr__(self):
        return '(Name: {0} Value {1})'.format(self.name, self.binarySignal)

Hello = Brain(10000, 100)

