class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self,r=None):
        self.root = Node(r)

    def addNode(self,data):
       
        queue = []
        queue.append(self.root)
        
        while True:
            node = queue.pop(0)
            if node.left is None:
                node.left = Node(data)
                break
            if node.right is None:
                node.right = Node(data)
                break

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return
    
    def BFS(self):
        queue = []
        queue.append(self.root)
        
        while len(queue):
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return
    
    def print_specific_level(self):
        queue = []
        level = 0
        queue.append((self.root,level))
        
        while len(queue):
            node,l = queue.pop(0)
            if level != l:
                print()
                level=l
            print(node.data,end=" ")

            if node.left:
                queue.append((node.left,l+1))
            if node.right:
                queue.append((node.right,l+1))
        print()
        return



bt = BinaryTree(5)

bt.addNode(4)
bt.addNode(6)
bt.addNode(2)
bt.addNode(3)
bt.addNode(7)
bt.addNode(8)

# bt.print_level_order()
bt.print_specific_level()

# print(bt.root.data)
# print(bt.root.left.data)
# print(bt.root.right.data)
# print(bt.root.left.left.data)
# print(bt.root.left.right.data)
# print(bt.root.right.left.data)
# print(bt.root.right.right.data)