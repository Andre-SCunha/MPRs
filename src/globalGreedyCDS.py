import sys
import ast

Graph = {}
MPRs = {}

def readingGraph():
    with open(sys.argv[1], 'r') as f:
        s = f.read()
        global Graph
        Graph = ast.literal_eval(s)

def findBestNode(CurrSet):
    best = None
    bestLen = 0
    for node in Graph:
        if (best == None):
            best = node
        elif (len(set(Graph[node]) - CurrSet) > bestLen):
            best = node
            bestLen = len(set(Graph[node]) - CurrSet)
    return best

def globalGreedyCDS():
    CDS = set()
    while (len(set(Graph.keys() - CDS))>0):
        best = findBestNode(CDS)
        CDS.add(best)
        #Mudar pra reacheble (o loop tá errado)





readingGraph()
globalGreedyCDS()
