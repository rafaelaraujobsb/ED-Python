# Binary Search Tree
class Node:
	def __init__(self, element):
		self.element = element
		self.left = None
		self.right = None

	# get e set do elemento(nó)
	def getElement(self):
		return self.element

	def setElement(self, element):
		self.element = element

	# get e set da esquerda do elemento
	def getLeft(self):
		return self.left

	def setLeft(self, element):
		self.left = element

	# get e set da direita do elemento
	def getRight(self):
		return self.right

	def setRight(self, element):
		self.right = element

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, element):
		new = Node(element)

		if self.empty():
			self.root = new
		else:
			current = self.root

			while True:
				if current != None:
					dady = current

					current = (current.getLeft() if current.getElement() > element else current.getRight())
				else:
					break

			dady.setLeft(new) if dady.getElement() > element else dady.setRight(new)

	def remove(self, element):
		if !self.empty():
			current = self.root
			dady = None

			

	def searchMinDir(self, current):
		dady = current
		current = current.getLeft()

		while current.getLeft() != None:
			dady = current
			current = current.getLeft()

		current = current.getElement() # armazenando o valor do último nó
		dady.setLeft() = None # removendo o valor da bst

		return current # retorna o valor

	def empty(self):
		if self.root == None:
			return True
		return False


	def preOrdem(self, current):
		'''
			Raiz, Esq, Dir
		'''
		if current != None:
			print(current.getElement(), end=' ')
			self.preOrdem(current.getLeft())
			self.preOrdem(current.getRight())

	def getRoot(self):
		return self.root

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)
bst.preOrdem(bst.getRoot())
print()
