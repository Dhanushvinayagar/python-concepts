

class Grpah:

    def __init__(self):
        self.graph_data = {}

    def add_vertex(self,data):
        if self.graph_data.get(data):
            print("Vertex already there ", data)
            return
        self.graph_data[data] = []

    def print_graph(self):
        print("-------------Grpah Details-------------")
        for vertex,neighbours in self.graph_data.items():
            print("Vertex:", vertex , "->",neighbours)
        print("---------------------------------------")
        print()
        return

    def add_edge(self,vertex1,vertex2,is_directed):
        if self.graph_data.get(vertex1,None) is None:
            print("Vertex ",vertex1, "is not there")
            return
        if self.graph_data.get(vertex2) is None:
            print("Vertex ",vertex2, "is not there")
            return
        if is_directed:
            self.graph_data[vertex1].append(vertex2)
            self.graph_data[vertex2].append(vertex1)
            return
        
        self.graph_data[vertex1].append(vertex2)
        return
    
    def BFS(self,vertex):
        queue = []
        queue.append(vertex)
        visited=[]

        while len(queue):
            e = queue.pop(0)
            if e not in visited:
                print(e)
                visited.append(e)

                for v in self.graph_data[e]:
                    queue.append(v)

        return 
    
    def DFS(self,vertex,visited=[]):
        
        if vertex in visited:
            return
        
        print(vertex)
        visited.append(vertex)
        for v in self.graph_data[vertex]:
            self.DFS(v,visited)

        return
    
g = Grpah()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

# g.print_graph()

g.add_edge(1,2,True)
g.add_edge(2,3,False)
g.add_edge(3,6,True)
g.add_edge(4,1,True)
g.add_edge(4,5,False)
g.add_edge(5,6,True)


g.print_graph()

# g.DFS(1)
# g.BFS(1)