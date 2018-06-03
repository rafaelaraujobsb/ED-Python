class Grafo:
	def __init__(self, vertices):
		self.vertices = vertices
		self.grafo = [[0]*vertices for _ in range(vertices)]

	def addVertice(self, v, u):
		self.grafo[v-1][u-1] = 1
		self.grafo[u-1][v-1] = 1

	def temLigacao(self, v, u):
		if self.grafo[v-1][u-1] == 1:
			return True
		return False

	def show(self):
		for i in self.grafo:
			for j in i:
				print(j, end=" ")
			print()

	def bfs(self, v):
		visitados = [False]*self.vertices
		visitados[v-1] = True
		distancia = [0]*self.vertices
		#insere v na fila
		fila = [v-1]
		print("Raiz: %d" %v)

		while(len(fila) > 0):
			v = fila[0]

			for u in range(self.vertices):
				if self.grafo[v][u] == 1 and not visitados[u]:
					visitados[u] = True
					fila.append(u)
					print("%d visitado" %(u+1))
			fila.pop(0)


g = Grafo(5)
'''g.addVertice(1,2)
g.addVertice(1,3)
g.addVertice(1,4)
g.addVertice(2,5)
g.addVertice(3,6)
g.addVertice(3,7)
g.addVertice(4,8)
g.addVertice(5,9)
g.addVertice(6,10)
'''
g.addVertice(1,4)
g.addVertice(4,2)
g.addVertice(4,5)
g.addVertice(2,5)
g.addVertice(3,5)

g.bfs(1)

g.show()
