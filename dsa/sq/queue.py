class Queue:

    def __init__(self,size):
        self.arr = []
        self.size = size

    def enqueue(self,element):
        if len(self.arr) == self.size:
            print("Queue is already full")
            return 
        self.arr.append(element)
        print("Element ",element, " inserted")
        return
    
    def dequeue(self):
        if len(self.arr)==0:
            print("No element is there in Queue")
            return
        el = self.arr.pop(0)
        print("Element ",el," removed from Queue")
        return el
    
    def printl(self):
        print(self.arr)
        return
    
q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()