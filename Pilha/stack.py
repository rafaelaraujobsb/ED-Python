class Stack:
    def __init__(self):
        self.__stack = []
        self.__qtd = 0

    def push(self, n):
        self.__stack.append(n)
        self.__qtd += 1

    def pop(self):
        if not self.empty():
            self.__stack.pop(-1)
            self.__qtd -= 1

    def top(self):
        if not self.empty():
            print(str(self.__stack[-1]))

    def empty(self):
        if self.__qtd == 0:
            return True
        return False

s = Stack()
s.push(5)
s.push(1)
s.push(8)
s.push(7)
s.push(0)
s.pop()
s.pop()

s.top()
print(s.empty())

