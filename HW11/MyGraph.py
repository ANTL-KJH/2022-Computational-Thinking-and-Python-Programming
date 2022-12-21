# MyGraph.py
import sys

class Node(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src_nm, dest_nm):
        self.src_nm = src_nm
        self.dest_nm = dest_nm

    def getSource_nm(self):
        return self.src_nm

    def getDestination_nm(self):
        return self.dest_nm

    def __str__(self):
        return "{:3}->{:3}".format(self.src_nm, self.dest_nm)

class WeightedEdge(Edge):
    def __init__(self, src_nm, dest_nm, weight=1.0):
        Edge.__init__(self, src_nm, dest_nm)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return "({}->{}:{:3})".format(self.src_nm, self.dest_nm, self.weight)


class WeightedGraph(object):
    def __init__(self,):
        self.nodes = [] # list of Node(v_id, v_names)
        self.node_names = []
        self.wedges = [] # list of weighted_edges
        self.adjacencyList = {} # dict of {src_nm:list of node_names)
        self.edgeWeights = {} # dictionary of {edge(src_nm, dest_nm):weight}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicated node")
        else:
            self.nodes.append(node)
            node_nm = node.getName()
            self.node_names.append(node_nm)
            self.adjacencyList[node_nm] = []

    def addEdge(self, weighted_edge):
        src_nm = weighted_edge.getSource_nm()
        dest_nm = weighted_edge.getDestination_nm()
        if not (src_nm in self.node_names and dest_nm in self.node_names):
            raise ValueError("Node not in graph")
        self.wedges.append(weighted_edge)
        self.adjacencyList[src_nm].append(dest_nm)
        self.edgeWeights[(src_nm, dest_nm)] = weighted_edge.getWeight()

    def getNeighbors(self, node_nm):
        #print(" WeightedGraph::getNeighbors({}) = {}".format(node_nm, self.adjacencyList[node_nm]))
        return self.adjacencyList[node_nm]

    def getAdjacencyList(self):
        return self.adjacencyList

    def getNode_NMs(self):
        return self.node_names

    def getWEdges(self):
        return self.wedges

    def getEdgeWeight(self, edge):
        if (edge.src_nm, edge.dest_nm) in self.edgeWeights:
            return self.edgeWeights[(edge.src_nm, edge.dest_nm)]
        else:
            None

    def printConnectivity(self):
        print("\nInter-City Connectivity Table:")
        print("     |", end="")
        for i in range(len(self.node_names)):
            print("{:>5}".format(self.node_names[i]), end="")
        print("\n-----+", end="")
        for i in range(55):
            print("-", end="")
        print()
        for i in range(len(self.node_names)):
            print(" {:4}|".format(self.node_names[i]), end="")
            for p in range(len(self.node_names)):
                if self.node_names[i] == self.node_names[p]:
                    print("{:>5}".format(0), end="")
                elif (self.getEdgeWeight(Edge(self.node_names[i], self.node_names[p])) != None):
                    print("{:>5}".format(self.getEdgeWeight(Edge(self.node_names[i], self.node_names[p]))), end="")
                else:
                    print("{:>5}".format("oo"), end="")
            print()

    def printEdges(self):
        eCount = 0
        for e in self.wedges:
            print(" {}".format(e), end=', ')
            eCount += 1
            if eCount % 5 == 0:
                print()

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
                return result[:-1]  # omit final newline




def printPath(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result

PLUS_INF = sys.maxsize # define as max of integer
def Dijkstra(G, start_nm, end_nm):
    errorInLoop = False
    nodeAccWeight = {}  # dictionary of node:accumulated_weight_from_start
    nodeStatus = {}
    prevNodes_nm = {}  # previous node in the path from the start to the end
    selectedNodes = []
    remainingNodes = []
    wEdges = G.getWEdges()
    # print("Dijkstra::edges : ", edges)
    for node_nm in G.node_names:
        e = Edge(start_nm, node_nm)
        if node_nm == start_nm:
            eWeight = 0
        else:
            eWeight = G.getEdgeWeight(e)
            if eWeight == None:
                eWeight = PLUS_INF
        # print(" Initial weight of edge ({}) = {}: ".format(e, eWeight))
        nodeAccWeight[node_nm] = eWeight
        nodeStatus[node_nm] = False  # not selected yet
        prevNodes_nm[node_nm] = start_nm
        if node_nm != start_nm:
            remainingNodes.append(node_nm)
    nodeAccWeight[start_nm] = 0
    nodeStatus[start_nm] = True
    selectedNodes.append(start_nm)
    # print("nodeAccWeight : ", nodeAccWeight)
    # print("Initial status of prevNode : ", prevNodes_nm)
    count = 1
    while len(remainingNodes) != 0:
        # print(">>> Round {} :".format(count))
        minAccWeight = PLUS_INF
        minNode = None
        # print(" -- currently selected {}, remaining {}".format(selectedNodes, remainingNodes))
        for n in remainingNodes:
            nAccWeight = nodeAccWeight[n]
            # print(" -- evaluating node ({:3}), nAccWeight({}) ...".format(n, nAccWeight))
            # print(" -- current minAccWeight = ", minAccWeight)
            if ((nAccWeight != None) and (nAccWeight < minAccWeight)):
                minNode, minAccWeight = n, nodeAccWeight[n]
                # print(" ==> minAccWeight updated by newMinNode ({}) with minAccWeight({})".format(minNode, minAccWeight))
        if minNode == None:
            print("No minNode was selected at this round !!")
            print("Error - graph is not fully connected !!")
            errorInLoop = True
            break
        else:
            # print(" -- newly selected minNode : {}".format(minNode))
            selectedNodes.append(minNode)
            minAccWeight = nodeAccWeight[minNode]
            # edge relaxations
            for rn in remainingNodes:
                if rn == minNode:
                    continue
                e = Edge(minNode, rn)
                eWeight = G.getEdgeWeight(e)
                # print(" -- eWeight({}->{}):{}".format(minNode, rn, eWeight))
                if eWeight == None:
                    continue
                if nodeAccWeight[rn] > minAccWeight + eWeight:
                    nodeAccWeight[rn] = minAccWeight + eWeight
                    prevNodes_nm[rn] = minNode
                # print(" -- Updated nodeAccWeight for node ({:3}) with prevNode({:3})".format(rn, minNode))
            if minNode == end_nm:
                # reached to destination
                break
            remainingNodes.remove(minNode)
        # print(" -- PrevNode : ", prevNodes_nm)
        # print(" -- Remaining nodes : ", end='')
        """
        for rn in remainingNodes:
        print("{} ({})".format(rn,nodeAccWeight[rn]), end=', ')
        print()
        """
        count += 1
            #
    if errorInLoop == True:
        return None
    #print(" prevNode : ", prevNodes_nm)
    path = [end_nm]
    cur_node_nm = end_nm
    while cur_node_nm in selectedNodes:
        # print("Current path : ", path)
        if cur_node_nm == start_nm:
            break
        else:
            cur_node_nm = prevNodes_nm[cur_node_nm]
            path.insert(0, cur_node_nm)
            # print("Current path : ", path)
    return path, nodeAccWeight[end_nm]