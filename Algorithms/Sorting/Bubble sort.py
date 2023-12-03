#Implementation of bubble sort algorithm
def bubbleSort(arr):
    n = len(arr)
    #Traverse thrugh all array elements
    for i in range(n):
        swapped = False

        #Last i elements are already in place
        for j in range(0, n-i-1):
            #Traverse the array from 0 to n-i-1 and swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    print(arr)
#Testing
bubbleSort([2,0,1])        