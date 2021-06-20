import heapq
class Solution:
    def countZeroes(self, A, N):
        
        output=[]
        
        for i in range(N):
            output.extend(A[i])
            
        heapq.heapify(output)
        count=0
        
        while output:
            x=heapq.heappop(output)
            
            if x==0:
                count+=1
                
        return count
