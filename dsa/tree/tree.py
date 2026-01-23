# tree with n nodes

class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

class Tree:

    def add_child(self,node,parent_id,id):
        
        if node.id == parent_id:
            node.children.append(Node(id))
            return
        
        for child in node.children:
            self.add_child(child,parent_id,id)
        
        return
    
    def print_children(self,node):
        print(node.id)
        for child in node.children:
            self.print_children(child)

    def print_tree(self,node,parent_id):

        if node.id == parent_id:
            print(node.id)
        
            for child in node.children:
                self.print_children(child)

        for child in node.children:
            self.print_tree(child,parent_id)

root = Node(10)

li = [(10,1),(10,2),(1,3),(1,4),(2,5),(2,6)]

tree = Tree()

for i in li:
    tree.add_child(root,i[0],i[1])

tree.print_tree(root,10)