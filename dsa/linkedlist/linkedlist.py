class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def createList(self,list):
        temp = self.root
        for data in list:
            if self.root is None:
                self.root = Node(data)
                temp = self.root
                self.size += 1
            else:
                temp.next = Node(data)
                temp = temp.next
                self.size += 1

    def printList(self):
        temp = self.root
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()
        print("-------------------")

    def reverseList(self):
        prev = None
        current = self.root
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.root = prev

    def sortList(self):
        
        if self.root is None:
            return
        
        res = Node(self.root.data)
        temp = self.root.next
        while temp:
            if res.data > temp.data:
                t = Node(temp.data)
                t.next = res
                res = t
            else:
                t = res
                while  t.next and temp.data > t.next.data:
                    t = t.next
                if t.next is None:
                    t.next = Node(temp.data)
                else:
                    x = t.next
                    t.next = Node(temp.data)
                    t.next.next = x
            temp = temp.next
        
        self.root = res
        return
        
ll = LinkedList()
ll.createList([3,1,5,4,2])
ll.printList()
ll.sortList()
ll.printList()
ll.reverseList()
ll.printList()
