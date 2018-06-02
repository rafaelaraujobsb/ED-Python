class Grafo:
	def __init__(self, vertices):
		self.vertices = vertices
		self.grafo = [[] for i in range(vertices)]

	def addVertice(self, u, v):
		'''
			Grafo Direcional
		'''
		self.grafo[u-1].append(v-1)

	def show(self):
		for index in range(self.vertices):
			print("%d: " %(index+1), end= " ")
			for j in self.grafo[index]:
				print("%d" %(j+1), end=" ")
			print()

g = Grafo(5)
g.addVertice(1,2)
g.addVertice(4,1)
g.addVertice(2,3)
g.addVertice(2,5)
g.addVertice(5,3)

g.show()

