import sys
import ast

Graph = {}

def readingGraph():
    with open(sys.argv[1], 'r') as f:
        s = f.read()
        global Graph
        Graph = ast.literal_eval(s)

def calcEssential(N1):
    dic = {}
    for n in N1:
        for n2 in Graph[n]:
            dic[n2] = 0
    for n in N1:
        for n2 in Graph[n]:
            dic[n2] += 1
    List = []
    for i in dic:
        if dic[i] == 1 and i not in N1:
            List.append(i)
    return List

def calcMPR(node):
    MPR = set()
    reach = set()
    neig = Graph[node]
    neig2 = set()
    for n in neig:
        neig2.update(Graph[n])
    neig2.difference_update(neig)
    reach.update(calcEssential(neig))
    for n in neig:
        if (len(set(Graph[n])&reach)>0):
            MPR.add(n)
    for n in MPR:
        reach.update(Graph[n])
    left = set(neig) - MPR
    left2 = (neig2 - reach)
    while(len(left2) > 0):
        best = None
        bestlen = -1
        for n in left:
            ln = len(set(Graph[n])&(left2))
            if(ln > bestlen):
                best = n
                bestlen = ln
            elif(ln == bestlen and len(set(Graph[n]) - left2) < len(set(Graph[best]) - left2)):
                best = n
        MPR.add(best)
        left.remove(best)
        left2.difference_update(Graph[best])
    return MPR



readingGraph()
#print calcEssential(Graph["a"])
print calcMPR(0)
