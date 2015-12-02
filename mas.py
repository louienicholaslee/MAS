import random

class masProblem():
    """ The 'agreed upon' data structure for a graph problem for the MAS program.
        The graph itself is stored as a tuple of tuples representing an adjacency matrix
        while the vertices are stored as a tuple, for example:

                   Graph:                     Adjacency Matrix:

                    [1]                         ((0, 1, 0, 0)
                     |                           (0, 0, 1, 1)
                     V                           (0, 0, 0, 1)
                    [2]                          (0, 0, 0, 0))
                     |
                    / \                         Vertex Tuple:
                   /   \
                  /     \                        (1, 2, 3, 4)
                [3] --> [4]

    """
    def __init__(self, adjMatrix, vertexTuple=None):
        """ Create a new masProblem with an adjacency matrix adjMatrix. """
        self.adjMatrix = adjMatrix
        self.length = len(adjMatrix)
        if vertexTuple is not None:
            self.vertexTuple = vertexTuple
        else:
            self.vertexTuple = tuple(i + 1 for i in range(self.length))
    
    def __str__(self):
        """ Print this object in a readable way... """
        length=len(self.adjMatrix)
        strlist=['n = ', str(length), '\nproblem adjacency matrix :\n [', str(self.adjMatrix[0])]
        for newLineIndex in range(length - 1):
            strlist.append('\n  ')
            strlist.append(str(self.adjMatrix[newLineIndex]))
        strlist.append(']\nvertices : ')
        strlist.append(str(self.vertexTuple))
        return ''.join(strlist)
    
    def copyMasProblem(self):
        """ Returns a copy of the current masProblem. """
        return masProblem(self.adjMatrix, self.vertexTuple)
        
    def removeVertex(self, vertex):
        """ Removes a vertex from and returns a copy of this masProblem. """
        return self.removeVertices((vertex,))
    
    def removeVertices(self, vertexList):
        """ Removes all vertices in vertexList from and returns a copy of this masProblem. """
        newMasProblem = self.copyMasProblem()
        newMasProblem.localRemoveVertices(vertexList, masProblem.toPositionDict(vertexList))
        return newMasProblem
    
    def masForwardCheck(self, vertexOrdering):
        """ Calculates the number of forward edges of a mas for the current problem."""
        positionDictionary = masProblem.toPositionDict(vertexOrdering)
        totalForward = 0
        for adjListIndex in range(self.length):
            for targetIndex in range(self.length):
                if self.adjMatrix[adjListIndex][targetIndex] == 1:
                   if positionDictionary[self.vertexTuple[adjListIndex]] < positionDictionary[self.vertexTuple[targetIndex]]:
                       totalForward = totalForward + 1
        return totalForward
    
    def localRemoveVertices(self, vertexList, positionDict):
        """ directly remove a vertex from this instance of a masProblem. """
        self.adjMatrix = list(masProblem.transpose(self.adjMatrix))
        self.vertexTuple = list(self.vertexTuple)
        if len(vertexList) == self.length:
            self.adjMatrix = ()
            self.vertexTuple = ()
            self.length = 0
            return
        for vertex in vertexList:
            self.vertexTuple.remove(vertex)
            self.adjMatrix.remove(self.adjMatrix[positionDict[vertex]])
        self.adjMatrix = list(masProblem.transpose(self.adjMatrix))
        for vertex in vertexList:
            self.adjMatrix.remove(self.adjMatrix[positionDict[vertex]])
        self.adjMatrix = tuple(self.adjMatrix)
        self.vertexTuple = tuple(self.vertexTuple)
        self.length = len(self.vertexTuple)

    @staticmethod
    def toPositionDict(vertexList):
        """ Converts a vertex ordering to a dictionary for the convenience of methods that
            need to reference a vertex's adjacency list in self.adjMatrix. "
            (4, 3, 2, 1) => {1:3, 2: 2, 3: 1, 4: 0}. """
        positionDictionary={}
        for i in range(len(vertexList)):
            positionDictionary[vertexList[i]] = i
        return positionDictionary
    
    @staticmethod
    def transpose(adjMatrix):
        return tuple(zip(*adjMatrix))
    
    @staticmethod
    def sumCols(adjMatrix):
        """ Sums the columns of an adjacency matrix. Returns an ordered tuple of sums. """
        return sumRows(transpose(adjMatrix))
    
    @staticmethod
    def sumRows(adjMatrix):
        """ Sums the rows of an adjacency matrix. Returns an ordered tuple of sums. """
        return tuple(reduce(lambda x,y: x+y, row) for row in adjMatrix)

def genRandArray(n):
    def random01(i, j):
        if i == j:
            return 0
        else:
            return random.randint(0, 1)
    return tuple(tuple(random01(i, j) for i in range(n)) for j in range(n))

def masDag(masProblem):
    """ Solves for the minimum acyclic graph of a problem by initially creating an approximate 
        ordering for the MAS. A local search update is then applied to look for a better ordering. 
        
        Graph G, split into dag of scc. Now we have a rough ordering set up via linear ordering of
        the scc's.
        In order, break up in scc:
            1. It splits the scc into a """
    
    return

def masBruteForce(masProblem):
    """ Solves for the minimum acyclic graph of a problem with a brute-force method; tries and
        check every single possible ordering. Uses ugly nonfunctional variables MaximumEdges
        and MaximumOrder to store the best orderings throughout the recursive calls. """
    MaximumEdges=[0]
    MaximumOrder=[()]
    def masSubproblem(masProblem,currentOrder,n):
        """ Non-functional recursive function that recurses down the possible orderings updating two
            'global' variables with the best order that has been found. """
        if len(currentOrder) == n:
            score = masProblem.masForwardCheck(currentOrder)
            if score > MaximumEdges[0]:
                MaximumEdges[0] = score
                MaximumOrder[0] = currentOrder
        else:
            for vertex in masProblem.vertexTuple:
                masSubproblem(masProblem.removeVertex(vertex), currentOrder + (vertex,), n)
    masSubproblem(masProblem, (), masProblem.length)
    return MaximumOrder[0]


def checkMasForward():
    exampleProblem = masProblem(((0, 1, 0, 0), (0, 0, 1, 1), (0, 0, 0, 1), (0, 0, 0, 0)))
    exampleSolution = (1, 2, 3, 4)
    return exampleProblem.masForwardCheck(exampleSolution)
    
def checkSkeleton():
    exampleProblem = masProblem(((0, 1, 0, 0), (0, 0, 1, 1), (0, 0, 0, 1), (0, 0, 0, 0)))
    exampleSolution = masBruteForce(exampleProblem)
    return exampleSolution == (1, 2, 3, 4)