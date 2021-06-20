import heapq
def kthSmallest(mat, n, k): 
    min_heap=[]
    for i in range(n):
        for j in range(n):
            heapq.heappush(min_heap,mat[i][j])
            
    while k:
        x=heapq.heappop(min_heap)
        k-=1
        
    return x
