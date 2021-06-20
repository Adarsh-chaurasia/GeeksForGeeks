class Solution:
    def sumOfMatrix(self,N,M,Grid):
        output=[]

        for i in range(N):
            output.extend(Grid[i])
            
        return sum(output)
      
      
//it takes O(N) times.
