def insert(stack,temp):
    if len(stack)==0 or stack[0]<=temp:
        stack.insert(0,temp)
        return
    
    val=stack.pop(0)
    insert(stack,temp)
    
    stack.insert(0,val)
    
    return

def sorted(s):
    if len(s)==1:
        return 1
    temp=s.pop(0)
    sorted(s)
    insert(s,temp)
    return 

