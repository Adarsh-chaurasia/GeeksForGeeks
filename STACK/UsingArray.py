class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.data=data
        self.arr.append(self.data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr):
            return self.arr.pop()
        else:
            return -1
