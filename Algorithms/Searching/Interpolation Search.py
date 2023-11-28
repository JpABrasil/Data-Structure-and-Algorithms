#Implementation of a interpolation search with a recursive function
def interpolationSearch(arr,lo,hi,x):
    '''
    arr: Array where you are searching
    lo: lower index of the search interval
    high: Higher index of the search interval
    x: Target
    pos: Position to search
    '''
    #Check if the target is in the range defined
    if(lo <= hi and x >= arr[lo] and x <= arr[hi]):
        #Probing the position with keeping uniform distrubution in mind
        pos = lo + ((hi-lo) // (arr[hi]-arr[lo]) * (x-arr[lo]))

        #Condition of target found
        if arr[pos] == x:
            return pos
        
        #If x is larger, x is in the right subarray
        if arr[pos] < x:
            return interpolationSearch(arr,pos+1,hi,x)
        
        #If x is smaller, x is in the left subarray
        if arr[pos] > x:
            return interpolationSearch(arr,lo,pos-1,x)
        
    return "The target is not in the range"

#Tesiting
array = [0,1,2,3,4,5,6,7,8,9,10]
target = 3
result = interpolationSearch(array,0,len(array)-1,target)
print(result) 

#Second test
target = 33
result = interpolationSearch(array,0,len(array)-1,target)
print(result) 