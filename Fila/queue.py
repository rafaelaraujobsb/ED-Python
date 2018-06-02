# -*- coding: utf-8 -*-

class Queue:
	def __init__(self):
		self.__queue = []
		self.__qtd = 0

	def push(self, n):
		self.__queue.append(n)
		self.__qtd += 1

	def pop(self):
		if not self.empty():
			self.__queue.pop(0)
			self.__qtd -= 1

	def front(self):
		if not self.empty():
			print(self.__queue)
		else:
			print("Fila vázia")
	def empty(self):
		if self.__qtd == 0:
			return True
		return False

q = Queue()
q.push(10)
q.push(50)
q.push(25)
q.pop()
q.front()
q.pop()
q.front()
q.pop()
q.front()

