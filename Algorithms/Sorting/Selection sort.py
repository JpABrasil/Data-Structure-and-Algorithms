#Implementation of selection sorting
def selectionSorting(arr):
    for i in range(len(arr)):
        #Defining the minimum index as the position i
        min_idx = i
        #Checking every position after the position i
        for j in range(i+1, len(arr)):
            #if the number in the position i is greather then a number in position j
            if arr[min_idx] > arr[j]:
                #Makes min_idx equals to j
                min_idx = j
        #Swap the values in the position i and position min_idx(that its equal to the position j if the number in position j its smaller then the number in position i)        
        arr[i], arr[min_idx] = arr[min_idx],arr[i]
    print(arr)

#Testing
selectionSorting([2,0,1])