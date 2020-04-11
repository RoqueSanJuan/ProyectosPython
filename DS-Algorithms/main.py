
import Stack

def is_paren_balanced(paren_string):
    """
    La siguiente funcion se encarga de controlar de un string esta balanceado o no dependiendo de la cantidad
    de ( ) que contiene , ejemplo balanceado : ()()   ejemplo no balanceado: (()
    """
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)   #Si es uno de los caracteres de incio , lo ingreso en la pila
        else:
            if s.is_empty():
                is_balanced = False   #Si no es de inicio , y esta vacio , significa que no esta balanceado ejm: ]]
            else:
                top = s.pop()         #Si no es inicio , y no esta vacio el stack saco uno
                if not is_match(top, paren):
                    is_balanced = False       #Si no machea con el que estaba en el top , es falso
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False



myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

print(myStack.items[-2])