class Grafo:
	'''
		Usando matriz de adjacencia
	'''

	def __init__(self, vertices):
		self.vertices = vertices
		self.grafo = [[0]*vertices for _ in range(vertices)]
		self.visitados = [False]*vertices

	def addVertice(self, v, u):
		self.grafo[v-1][u-1] = 1
		self.grafo[u-1][v-1] = 1

	def show(self):
		for i in self.grafo:
			for j in i:
				print(j, end=" ")
			print()

	def temLigacao(self, u, v):
		if self.grafo[u-1][v-1] == 1:
			return True
		return False

	def dfs(self, v):
		'''
			Função recursiva para busca em profundidade
		'''
		self.visitados[v-1] = True
		print("%d visitado" %v)
		for i in range(self.vertices):
			if self.grafo[v-1][i] == 1 and self.visitados[i] == False:
				self.dfs(i+1)

g = Grafo(5)
g.addVertice(1, 4)
g.addVertice(2, 4)
g.addVertice(2, 5)
g.addVertice(4, 5)
g.addVertice(5, 3)
g.show()

print(g.temLigacao(3, 4))
g.dfs(1)

