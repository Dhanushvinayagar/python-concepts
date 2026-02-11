class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def add(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # def heapify_up(self, index):
    #     while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
    #         p = self.parent(index)
    #         self.heap[p], self.heap[index] = self.heap[index], self.heap[p]
    #         index = p

    def heapify_up(self,index):
        parent = self.parent(index)
        if parent<0:
            return
        if self.heap[parent]<=self.heap[index]:
            return
        
        self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
        index=parent
        self.heapify_up(index)

    def peek(self):
        if not len(self.heap):
            return 'Empty heap'
        return self.heap[0]
    
    def pop(self):
        if not len(self.heap):
            print("noting to pop")
            return
        last_element = self.heap.pop()
        self.heap[0] = last_element
        self.heapify_down(0)
        return 
    
    def heapify_down(self,parent):

        if parent>=len(self.heap):
            return 
        l = self.left(parent)
        if l>=len(self.heap):
            return 
        
        r = self.right(parent)
        if r>=len(self.heap):
            if self.heap[l] < self.heap[parent]:
                self.heap[parent],self.heap[l]=self.heap[l],self.heap[parent]
            return
       
        if self.heap[l] > self.heap[r]:
            if self.heap[r] < self.heap[parent]: 
                self.heap[parent],self.heap[r]=self.heap[r],self.heap[parent]
                self.heapify_down(r)    
            return
        elif self.heap[l] < self.heap[parent]: 
            self.heap[parent],self.heap[l]=self.heap[l],self.heap[parent]
            self.heapify_down(l)
            return

    def print_heap(self):
        print(self.heap)

h = MinHeap()
h.add(3)
h.add(2)
h.add(1)
h.add(5)
h.add(4)
h.add(6)
h.add(8)
h.add(7)
h.add(0)

# h.add(5)
# h.add(9)
# h.add(6)
# h.add(10)
# h.add(8)
# h.add(-7)
# h.add(4)
# h.add(3)

h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
h.pop()
h.print_heap()
