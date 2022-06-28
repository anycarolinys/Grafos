import networkx as nx
import queue

NIL = 0 # global
INF = float('inf')

class HopcroftKarp:
    def __init__(self, B: nx.Graph):
        self.B = B
        l, r = nx.bipartite.sets(B)
        self.m = len(l)
        self.n = len(r)
        self.pairU = [0] * (self.m + 1)
        self.pairV = [0] * (self.n + 1)
        self.dist = [0] * (self.m + 1)

    def BFS(self):
        q = queue.Queue()
        
        for u in range(1,self.m):
            if self.pairU[u] == NIL:
                self.dist[u] = 0
                q.put(u)
            else:
                self.dist[u] = INF
        
        self.dist[NIL] = INF
        
        while not q.empty():
            u = q.get()
            
            if self.dist[u] < self.dist[NIL]:
                # for vertex in list(self.B[u]):
                for v in range(len(self.B[u])):
                    # v = vertex
                    
                    # print(u)
                    # print(v)
                    if self.dist[self.pairV[v]] == INF:
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        q.put(self.pairV[v])
                        
        if self.dist[NIL] != INF:
            return True
        
        return False
    
    def DFS(self, u):
        if u != NIL:
            for v in range(len(self.B[u])):
                # v = vertex

                if self.dist[self.pairV[v]] == self.dist[u]+1:
                    if self.DFS(self.pairV[v]):
                        self.pairV[v] = u
                        self.pairU[u] = v
                        return True
            self.dist[u] = INF
            return False
        
        return True
    
    def HopcroftKarpAlgorithm(self):
        
        for u in range(self.m):
            self.pairU[u] = NIL
            
        for v in range(self.n):
            self.pairV[v] = NIL
            
        result = 0
        
        while self.BFS():
            for u in range(1,self.m):
                if self.pairU[u] == NIL and self.DFS(u):
                    result += 1
                    
        return result


if __name__ == "__main__":
    B = nx.Graph()
    top_nodes = ['B','E','J','L','T','A','R']
    B.add_nodes_from(top_nodes, bipartite=0)
    bottom_nodes = [1,2,3,4,5,6,7]
    B.add_nodes_from(bottom_nodes, bipartite=1)

    B.add_edges_from([('B',1),('B',4),('E',7),('E',3),('E',6),('J',2),('J',5),('J',4),('L',7),('L',2),('T',7),('T',6),('T',5),('A',3),('A',6),('R',6),('R',7)])

    IntegerBipartite = nx.convert_node_labels_to_integers(B)


    # print(nx.is_bipartite(IntegerBipartite))

    HK = HopcroftKarp(IntegerBipartite)
    top, bottom = nx.bipartite.sets(IntegerBipartite)
    print(top)
    print(bottom)
    
    print(HK.HopcroftKarpAlgorithm())
    
    #Obtain the maximum cardinality matching
    my_matching = nx.bipartite.matching.hopcroft_karp_matching(IntegerBipartite, top)
    print(my_matching)
    print(len(my_matching))
    