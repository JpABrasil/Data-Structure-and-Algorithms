#This is an implementation with a recursive funciton it is possible to do with an while loop(iterative version)
def ternarySearch(arr,l,r,x):
    '''
    arr: Array that you are searching into
    l: Left index of the array
    r: Right index
    x: Target
    '''
    if (r>=l):
        #Find mid1 and mid2
        mid1= l + (r-l) //3
        mid2= r - (r-l) //3

        #Check if the key is present at any mid
        if (arr[mid1] == x):
            return mid1
        if (arr[mid2] == x):
            return mid2
        
        #Since the key is not present in any mid check in which region it is present then repeat the search in that region
        if(x<arr[mid1]):
            #The key its in the first third
            return ternarySearch(arr,l,mid1-1,x)
        elif (x > arr[mid2]):
            #The key its in the third third
            return ternarySearch(arr,mid2 +1,r,x)
        else:
            #The key its in the second third
            return ternarySearch(arr,mid1+1,mid2-1,x)
        

#Testing
array = [1,2,3,4,5,6,7,8,9,10]
target = 6
left_index = 0
right_index = len(array) - 1
result = ternarySearch(array,left_index,right_index,target)
print(result)