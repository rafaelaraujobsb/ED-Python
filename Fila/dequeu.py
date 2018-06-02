class Dequeu:
	def __init__(self):
		self.__dequeu = []
		self.__qtd = 0

	def empty(self):
		if self.__qtd == 0:
			return True
		return False

	def push_front(self, n):
		self.__dequeu.insert(0, n)
		self.__qtd += 1

	def push_back(self, n):
		self.__dequeu.append(n)
		self.__qtd += 1

	def pop_front(self):
		if not self.empty():
			self.__dequeu.pop(0)
			self.__qtd -= 1

	def pop_back(self):
		if not self.empty():
			self.__dequeu.pop(-1)
			self.__qtd -= 1

	def front(self):
		if not self.empty():
			print(self.__dequeu[0])

	def back(self):
		if not self.empty():
			print(self.__dequeu.pop[-1])

	def show(self):
		if not self.empty():
			print(self.__dequeu)


dq = Dequeu()
dq.push_back(1)
dq.push_back(5)
dq.push_back(9)
dq.push_front(0)
dq.show()

dq.pop_front()
dq.pop_back()
dq.show()

