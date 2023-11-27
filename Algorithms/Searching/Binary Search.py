def iterative_binary_search(arr,x):
    '''
    arr: Array where you are searching
    l: Left indice of the search interval
    r: Right indice of the search interval
    x: Target
    '''
    l = 0
    r = len(arr) - 1                    #The last position index is the lenght of the array minus 1
    while l <= r:                       #While the left index and right index of the search not equal
    
        mid = (l+r)//2                  #The mid of the search its 
    
        #Check if x is at the mid
        if arr[mid] == x:
            return mid                  #Return the position in the array of the taget

        #If x is greater, ignore the left half
        elif arr[mid] < x:
            l = mid + 1    

        #If x is smaller, ignore the right half
        else:
            r = mid -1
    
    #If we reach here, than the element was not present
    return "Not found"

#Testing the iterative version
array = [10,20,30,40,50]
target = 10
result = iterative_binary_search(array,target)
print(result)

def recursive_binary_search(arr,l,r,x):
    '''
    arr: Array where you are searching
    l: Left indice of the search interval
    r: Right indice of the search interval
    x: Target
    '''
    if r >= l:                              #If the righ index its bigger then the left

        mid = (l+r)//2

        #If the element is present in the middle itself
        if arr[mid] == x:
            return mid
        
        #If the mid value is greaten than then the target, then it can only be present in the left subarray
        elif arr[mid] > x:
            return  recursive_binary_search(arr,l,mid-1,x)
        
        #Else can only be in the right subarray
        else:
            return recursive_binary_search(arr,mid+1,r,x)
        
    else:
        return "Not found"

#Testing the recursive version
array = [10,20,30,40,50]
target = 30
result = recursive_binary_search(array,0,len(array)-1,target)
print(result)
