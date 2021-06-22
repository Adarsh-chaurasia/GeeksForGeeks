def findMax(arr):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if (mid-1)>=0 and arr[mid]>arr[mid-1] and (mid+1)<=len(arr) and arr[mid]>arr[mid+1]:
            return arr[mid]
        elif (mid-1)>= 0 and arr[mid-1]>arr[mid]:
            high=mid-1
        else:
            low=mid+1
    
    return arr[high]
arr=[2,4,16,19,20,9,7,5,3,2,1,]

print(findMax(arr))
