import sys
import ast

Graph = {}
MPRs = {}

def readingGraph():
    with open(sys.argv[1], 'r') as f:
        s = f.read()
        global Graph
        Graph = ast.literal_eval(s)

def calcEssential(S):
    dic = {}
    for n in S:
        for k in Graph[n]:
            dic[k] = 0
    for n in S:
        for k in Graph[n]:
            dic[k] += 1
    List = []
    for i in dic:
        if dic[i] == 1 and i not in S:
            List.append(i)
    return List

def calcMPR(node):
    neig = set(Graph[node])
    S = []
    U = set([])
    for n in neig:
        t = (n, [])
        for n2 in Graph[n]:
            if n2 not in neig and n2 != node:
                t[1].append(n2)
                U.add(n2)
        S.append(t)
    S = sorted(S, key = lambda t: -len(t[1]))
    return setCover(S,U)[0]



readingGraph()
print calcEssential(Graph["a"])
#print calcMPR(0)
