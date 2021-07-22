def bfsOfGraph(self, V, adj):
        visited=[False]*(V)
        
        output=[]
        
        queue=[]
        
        queue.append(0)
        visited[0]=True
        
        while queue:
            s=queue.pop(0)
            output.append(s)
            
            for node in adj[s]:
                if not visited[node]:
                    queue.append(node)
                    visited[node]=True
                    
        return output
