import sys
import ast

Graph = {}
MPRs = {}

def readingGraph():
    with open(sys.argv[1], 'r') as f:
        s = f.read()
        global Graph
        Graph = ast.literal_eval(s)

def setCover(S, U):#sorted S
    if(len(U)==0):
        return [set([]), True]
    elif(len(S) == 0):
        return [set([]), False]
    C1 = setCover(S[1:],U-set(S[0][1]))
    C1[0] |= set([S[0][0]])
    C2 = setCover(S[1:], U)
    if(C1[1] and C2[1]):
        if(len(C1[0]) < len(C2[0])):
            return C1
        else:
            return C2
    elif(not C1[1] and not C2[1]):
        return [set([]), False]
    else:
        return C1 if C1[1] else C2



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
    print setCover(S,U)



readingGraph()
calcMPR("a")
s1 = set([0,2,3])
s2 = set([2,6])
print s1 if len(s1)<len(s2) else s2
