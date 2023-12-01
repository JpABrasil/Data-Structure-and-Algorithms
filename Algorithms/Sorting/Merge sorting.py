#Implementation Merge Sort algorithm
def mergeSort(arr):
    #If the arr have more than 1 number
    if len(arr)>1:
        #find the mid of the arr
        mid = len(arr)//2
        #Dividing the arr elements
        left = arr[:mid]
        right =arr[mid:]
        
        #Sorting the first half
        mergeSort(left)
        #Sorting the second half
        mergeSort(right)

        i = j = k = 0
        
        #Copy data to temporary arrays left[] and right[]
        #While i smaller then the size of the left array and j smaller then the size of the right array
        while i < len(left) and j < len(right):
            if left[i] <= right [j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        #Check if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] =  right[j]
            j += 1
            k += 1
    return(arr)

#Testing 
test = mergeSort([2,0,1])
print(test)