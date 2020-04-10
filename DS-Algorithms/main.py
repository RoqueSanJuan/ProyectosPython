"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

print(myStack.get_stack())