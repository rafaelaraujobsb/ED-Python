class Grafo:
	def __init__(self, vertices):
		self.vertices = vertices
		self.grafo = [[0]*vertices for i in range(vertices)]

	def addAresta(self, u, v): 
		'''
			grafo bidirecional
		'''
		self.grafo[u-1][v-1] = 1
		self.grafo[v-1][u-1] = 1

	def show(self):
		for i in self.grafo:
			for j in i:
				print(j, end = ' ')
			print()


	def temLigacao(self, u, v):
		if self.grafo[u-1][v-1] == 1:
			return True
		return False

g = Grafo(5)
g.addAresta(1,3)
g.addAresta(3,4)
g.addAresta(2,3)
g.addAresta(3,5)
g.addAresta(4,5)
g.show()
print("1 -> 4 %s" %g.temLigacao(1,4))
print("3 -> 4 %s" %g.temLigacao(3,4))
