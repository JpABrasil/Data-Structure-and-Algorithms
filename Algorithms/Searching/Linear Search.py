def search(arr,x):
    '''
    arr: The array or list where you want to seach
    N: (int) number of the elements the arr have
    x: Target value you want to find
    '''
    N = len(arr)
    for i in range(0,N):        #For i(index) in the range from 0 to N
        if (arr[i] == x):       #If the value of the array in that i(index) is equal to the target
            return i            #Return the index
    return -1                   #If not return -1

#Testing the implementation
array = [20,30,50,70,80]
target = 30
index_of_the_target=search(array,target)
print(index_of_the_target)