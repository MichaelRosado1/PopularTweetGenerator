import random

# We will define the graph in terms of vertices

class Vertex:
    def __init__(self, value): #value will be the word 
        self.value = value
        self.adjacent = {} #dictionary of nodes that have an edge from this vertex
        self.neighbors = []
        self.neighborsWeights = []
        
    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def addEdge(self, vertex, weight = 0):
        self.adjacent[vertex] = weight

    def incrementEdge(self, vertex):
        #we want to increment the edge count if it exists
        #if it doesn't exist yet, then .get will return 0
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1
    
    def getAdjacentNodes(self):
        return self.adjacent.keys()

    def probabilityMap(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighborsWeights.append(weight)

    def nextWord(self):
        return random.choices(self.neighbors, weights = self.neighborsWeights)[0]
    


class Graph:
    def __init__(self):
        self.vertices = {}

    def getVertexValue(self):
        #return the list of values stored in the vertices
        return set(self.vertices.keys())
        
    def addVertex(self, value):
        self.vertices[value] = Vertex(value)

    def getVertex(self, value):
        if value not in self.vertices:
            self.addVertex(value)
        return self.vertices[value]
    
    def getNextWord(self, currentVertex):
        return self.vertices[currentVertex.value].nextWord()
    
    def generateProbMapping(self):
        for vertex in self.vertices.values():
            vertex.probabilityMap()



