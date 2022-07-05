class Node:
    def __init__(self, ID):
        self.ID = ID
        self.visited = False
        self.preRequisites = []

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, ID):
        # Create or find node that already exists
        exists = False
        for node in self.nodes:
            if node.ID == ID:
                exists = True
                return node
        if not exists:
            node = Node(ID)
            self.nodes.append(node)
            return node
    def addEdge(self, IDStart, IDDestination):
        nodeStart = self.addNode(IDStart)
        nodeEnd = self.addNode(IDDestination)
        nodeStart.preRequisites.append(nodeEnd)

# StartID, PreRequisitID1, PreRequisitID2 ...
file = open("classes.txt")
graph = Graph()
for line in file.readlines():   #   0       1      2
    line = line.strip()
    classes = line.split(", ")  # ["142", "141", "140"]
    startID = classes[0]
    for destinationID in classes[1:]:
         graph.addEdge(startID, destinationID)

while True:
    userInput = input("Input a course number: ")

    startNode = None
    exists = False
    for node in graph.nodes:
        if node.ID == userInput:
          exists = True
          startNode = node
          break
    if not exists:
        print("Sorry, course is not available")
    if exists:
        break

def getPreRequisitDepth(node):  # Gets the depth of an edge
    if node.preRequisites == []:
        return 1
    maxDepth = 0
    for edgeNode in node.preRequisites:
        depth = 1 + getPreRequisitDepth(edgeNode)
        if depth > maxDepth:
            maxDepth = depth
    return maxDepth

print(f"Semester: {getPreRequisitDepth(startNode)}")