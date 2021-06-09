class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        minheap=[]
        for i in range(K):
            head=temp=arr[i]
            while head:
                temp=head.next
                head.next=None
                heapq.heappush(minheap,head.data)
                head=temp
                
        head=tail=None
        while minheap:
            data=heapq.heappop(minheap)
            node=Node(data)
            if head==None:
                head=node
                tail=head
            else:
                tail.next=node
                tail=tail.next
        return head
        
