#First implement a Binary Search
def binarySearch(arr,l,r,x):
    if r >= l:
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            return binarySearch(arr,mid+1,r,x)
        if arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
    else:
        return "Target not found"
    
#Now we implement a Exponential Search using our binary search
def exponentialSearch(arr,n,x):
    '''
    arr: Array you are looking into
    n: Array size
    x: Target
    '''
    #If the target it is in the first position
    if arr[0] == x:
        return 0
    
    #incrementing exponetial the size
    i = 1
    while i < n and arr[i] <= x:
        i = i*2

    #Use the binary search and use our incrementing to find the range 
    return binarySearch(arr,i//2,min(i,n-1),x)
    
#Testing
array = [0,2,3,4,5,6,7,8]
target = 7
array_size = len(array)
result = exponentialSearch(array,array_size,target)
print(result)