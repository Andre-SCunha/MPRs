import sys
import ast

Graph = {}
MPRs = set()

def readingGraph():
    with open(sys.argv[1], 'r') as f:
        s = f.read()
        global Graph
        Graph = ast.literal_eval(s)

def findBestNode(CurrSet, Reach):
    best = None
    bestLen = 0
    for node in Reach:
        if (best == None):
            best = node
            bestLen = len(set(Graph[node]) - CurrSet)
        elif (len(set(Graph[node]) - CurrSet) > bestLen):
            best = node
            bestLen = len(set(Graph[node]) - CurrSet)
    return best

def globalGreedyCDS():
    CDS = set()
    Reach = set()
    Reach.add(findBestNode(CDS, Graph))
    while (len(set(Graph.keys()) - CDS - Reach)>0):
        best = findBestNode(CDS, Reach)
        CDS.add(best)
        Reach.remove(best)
        Reach |= (set(Graph[best]) - CDS)
    return CDS

def calcMPR(node):
    return set(Graph[node]) & MPRs





readingGraph()
MPRs = globalGreedyCDS()
print MPRs