
class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None


class BST:

    def addNode(self, id, parent):
        if parent.id > id:
            if parent.left is None:
                parent.left = Node(id)
            else:
                self.addNode(id, parent.left)
        else:
            if parent.right is None:
                parent.right = Node(id)
            else:
                self.addNode(id, parent.right)
        return

    def printTree(self, node):
        if node is None:
            return
        print(node.id)
        self.printTree(node.left)
        self.printTree(node.right)

        return

    
    def DFS(self,node):
        if not node:
            return
        
        self.DFS(node.left)
        self.DFS(node.right)
        print(node.id)

    def BFS(self,node):
        q=[]
        q.append(node)
        while len(q):
            n = q.pop(0)
            print(n.id)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return

 
li = [5,1,3,6,8,2,4,7]
root = Node(li[0])

bst = BST()
for i in range(1,len(li)):
    bst.addNode(li[i],root)

# bst.printTree(root)
# bst.DFS(root)
bst.BFS(root)