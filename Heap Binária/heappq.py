import heapq

class Pessoa:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

#p =  Pessoa("Teste __repr__")
#print(p)

class FilaDePrioridade:
	def __init__(self):
		self._fila = []
		self._indice = 0

	def inserir(self, item, prioridade):
		'''
			Valores maiores tem prioridade maior que os demais,
			por isso o uso do - no parametro
		'''
		heapq.heappush(self._fila, (-prioridade, self._indice, item))
		self._indice += 1

	def remover(self):
		return heapq.heappop(self._fila)[-1]

fila = FilaDePrioridade()

fila.inserir(Pessoa("Jao"), 20)
fila.inserir(Pessoa("Rafael"), 16)
fila.inserir(Pessoa("felipe"), 5)
fila.inserir(Pessoa("zé"), 1)

print(fila.remover())
