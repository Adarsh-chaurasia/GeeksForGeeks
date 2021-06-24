def reverse(S):
    stack=[]
    
    for each in S:
        stack.append(each)
        
    s=""
    while stack:
        s+=stack.pop()
    return s
