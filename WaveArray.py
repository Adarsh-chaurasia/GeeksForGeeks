class Solution:
    #Complete this function
    #Function to sort the array into a wave-like array.
    def convertToWave(self,A,N):
        if N & 1:
            for i in range(0,N-1,2):
                A[i],A[i+1]=A[i+1],A[i]
        else:
            for i in range(0,N-1,2):
                 A[i],A[i+1]=A[i+1],A[i]
                 
                 
                 
        return A
