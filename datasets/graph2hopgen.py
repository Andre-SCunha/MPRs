import random

def generate(inf, sup):
	G = {}
	nodes = set([])
	num = sup+1
	G[0] = []
	for i in range(sup):
		G[0].append(i+1)
		G[i+1] = [0]
		m = random.randint(inf, sup)
		for j in range(m):
			if(random.random() < .9 and len( nodes - set(G[i+1]) ) > 0):
				n = random.choice(list(nodes - set(G[i+1])))
				G[i+1].append(n)
				G[n].append(i+1)
			else:
				G[i+1].append(num)
				G[num] = [i+1]
				num = num + 1
		for k in G[i+1][1:]:
			nodes.add(k)
	print G

generate(5, 30)
#1 5 (12)0.285s
#5 10 (29)0.285s
#5 20(66)2.948s
#5 30(95)-
#10 50(239)- 