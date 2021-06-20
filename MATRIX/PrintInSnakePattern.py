from collections import *

#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
        leftRight=True
        output=[]
        
        for i in range(len(matrix)):
            currentLevel=deque([])
            for j in range(len(matrix)):
                if leftRight:
                    currentLevel.append(matrix[i][j])
                    
                else:
                    currentLevel.appendleft(matrix[i][j])
            leftRight=not leftRight
            output.extend(currentLevel)
            
            
        return output
