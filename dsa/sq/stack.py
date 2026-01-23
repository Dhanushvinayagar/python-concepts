
class Stack:

    def __init__(self,size):
        self.arr = []
        self.size = size
    
    def push(self,element):
        if len(self.arr)==self.size:
            print("Stack size is full")
            return
        self.arr.append(element)
        print("Element ",element, " is added")
        return

    def pop(self):
        if len(self.arr)==0:
            print("Stack is already empty")
            return
        el = self.arr.pop()
        print("Last element ", el , "removed")
        return el
    
stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()