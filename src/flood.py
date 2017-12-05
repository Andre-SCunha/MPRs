import localGreedy
import globalGreedyCDS as globalGreedy
import setCover
import time

Graphs = [{},{},{},{},{}]
V = [10,25,50,75,100,125,150,200,250,500]
Dist = {}
def readGraphs(n, r):
    for i in range(5):
        with open("datasets/100x100/100x100/N" + str(n) + "/n" + str(n) + "r" + str(r) + "/100_" + str(n) + "_" + str(r) + "_"+ str(i+1) + ".txt", 'r') as f:
            for k in range(n+1):
                s = f.readline()
            for k in range(n):
                s = f.readline()
                Graphs[i][k] = []
                for j in range(n):
                    if(s[j*2] == '1'):
                        Graphs[i][k].append(j)

def clearGraphs():
    for i in Graphs:
        i.clear()

def calcDist(G, n):
    Dist.clear()
    q = [(n, 0)]
    Dist[n] = 0
    while(len(q) > 0):
        t = q.pop(0)
        for i in G[t[0]]:
            if(i not in Dist):
                Dist[i] = t[1]+1
                q.append((i, t[1]+1))
            
def flood(mod, n, G):
    mod.Graph = G
    reach = set([n])
    trans = set([n])
    ret, delay, tm = 0,0,0
    q = [(n, 0)]
    while(len(q) > 0):
        t = q.pop(0)
        t0 = time.clock()
        mpr = mod.calcMPR(t[0])
        tm = tm + time.clock() - t0
        for i in G[t[0]]:
            if(i in mpr and i not in trans):
                q.append((i,t[1]+1))
                trans.add(i)
            if(i not in reach):
                reach.add(i)
                delay = delay + t[1]+1 - Dist[i]
            else:
                ret = ret + 1
    return ret, delay, tm

def floodAll():
    for i in range(10):
        n = V[i]
        for j in range(3):
            r = (j+1)*25
            readGraphs(n, r)
            print n, r
            L,G,S = [[0,0,0],[0,0,0],[0,0,0]]
            for k in range(5):
                calcDist(Graphs[k], 0)
                t1 = flood(localGreedy, 0, Graphs[k])
                t2 = flood(globalGreedy, 0, Graphs[k])
                globalGreedy.MPRs.clear()
                if(n < 3):
                    t3 = flood(setCover, 0, Graphs[k])
                for l in range(3):
                    L[l] += t1[l]/5.0
                    G[l] += t2[l]/5.0
                    if(n < 3):
                        S[l] += t3[l]/5.0
            print L
            print G
            print S
            clearGraphs()


floodAll()
