class Node:
	def __init__(self, element):
		self.element = element
		self.next = None

	def getElement(self):
		return self.element

	def setElement(self, element):
		self.element = element

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.next = None
		self.last = None
		self.qtd = 0

	def empty(self):
		if self.qtd == 0:
			return True
		return False

	def push(self, element, index):
		new = Node(element)

		if self.empty():
			self.next = new
			self.last = new
		else:
			if index > self.qtd-1:
				self.last.setNext(new)
				self.last = new
			elif index == 0:
				new.setNext(self.next)
				self.next = new
			else:
				i = 1
				atual = self.next.getNext()

				while i != index-1:
					atual = atual.getNext()
					i += 1

				new.setNext(atual.getNext())
				atual.setNext(new)

		self.qtd += 1

	def pop(self, index):
		if not self.empty():
			if index == 0:
				self.next = self.next.getNext()
			else:
				i = 1
				atual = self.next.getNext()

				while i != index-1:
					atual = atual.getNext()
					i += 1

				atual.setNext(atual.getNext().getNext())

				if index == self.qtd:
					self.last = atual.getNext()

			self.qtd -= 1

	def show(self):
		node = self.next

		while node != None:
			print(node.getElement(), end=' ')
			node = node.getNext()

		print()


lkd = LinkedList()
lkd.push('Rafael', 0)
lkd.push('Joao', 0)
lkd.push('Ze', 0)
lkd.push('Ze 1', 2)
lkd.show()

lkd.pop(2)
lkd.pop(0)
lkd.show()
