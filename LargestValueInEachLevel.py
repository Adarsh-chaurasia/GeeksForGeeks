from collections import *

class Solution:
    def largestValues(self, root):
        largest=[]
        if not root:
            return largest
        queue=deque([])
        queue.append(root)
        while queue:
            currentlevel=[]
            for i in range(len(queue)):
                current=queue.popleft()
                currentlevel.append(current.data)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            largest.append(max(currentlevel))
            
        return largest
            
            
