from collections import defaultdict 
  class Graph: 
    def minDistance(self,dist,queue): 
        # Initialize min value and min_index as -1 
        minimum = float("Inf") 
        min_index = -1
          
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 
  
    def printPath(self, parent, j): 
          
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print j, 
            return
        self.printPath(parent , parent[j]) 
        print j, 
    def printSolution(self, dist, parent): 
        src = 0
        print("Vertex \t\tDistance from Source\tPath") 
        for i in range(1, len(dist)): 
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])), 
            self.printPath(parent,i) 
  
    def dijkstra(self, graph, src): 
  
        row = len(graph) 
        col = len(graph[0]) 
        dist = [float("Inf")] * row 
   
        parent = [-1] * row 
   
        dist[src] = 0
      
        queue = [] 
        for i in range(row): 
            queue.append(i) 
              
        while queue: 
   
            u = self.minDistance(dist,queue)  
              queue.remove(u)  
            for i in range(col): 
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
          self.printSolution(dist,parent) 
  
g= Graph() 


entries = list(map(int, gclstm_proposed.split())) 
  
matrix = np.array(entries).reshape(R, C) 
  
g.dijkstra(matrix,0)
