"""
Stack Data Structure.
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):      #ingresa un items
        self.items.append(item)

    def pop(self, item):       #saca el ultimo items
        self.items.pop()

    def get_stack(self):       #muestra los elementos del stack
        return self.items

    def is_empty(self):           #pregunta por si esta vacio
        return self.items == []

    def peek(self):                 #devuelve  el ultimo item ingresado pero no lo saca
        if not self.is_empty():
            return self.items[-1]