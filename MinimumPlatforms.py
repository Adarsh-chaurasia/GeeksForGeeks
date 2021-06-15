import heapq

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        minheap=[]
        arrive.sort()
        depart.sort()
        heapq.heappush(minheap,depart[0])
        for i in range(1,len(arrive)):
            if arrive[i]>=minheap[0]:
                heapq.heappop(minheap)
                
            heapq.heappush(minheap,depart[i])
            
        if len(minheap)<=K:
            return 1
        else:
            return 0
