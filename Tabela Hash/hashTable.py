
class HashTable:
	def __init__(self, tableSize):
		assert tableSize > 1, "o tamanho da tabela tem que ser positivo"
		'''if tableSize < 1:
			raise ValueError("o tamanho tem que ser positivo")
		'''
		self.tableSize = tableSize

		# criar slots
		self.tableSize = tableSize
		self.table = [[] for i in range(tableSize)]

	def hashFunc(self, key):
		return key % self.tableSize # retorna uma chave, que é o resto da divisão

	def insert(self, key):
		self.table[self.hashFunc(key)].append(key)

	def show(self):
		for lkdList in self.table:
			if lkdList:
				for key in lkdList:
					print("%d" %key, end = " ")

				print("")

	def search(self, key): 
		if key in self.table[self.hashFunc(key)]:
			return True
		return False


ht = HashTable(9)
ht.insert(19)
ht.insert(28)
ht.insert(20)
ht.insert(25)
ht.insert(5)
ht.insert(33)
ht.insert(15)
ht.insert(9)
ht.insert(18)

print(ht.search(27))

ht.show()
