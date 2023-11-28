def revArr(arr,start,end):
    if type(arr) == str:            #If the type of the input is str
        arr=list(arr)
        while start < end:           #While the start index is lower than the end index
            arr[start],arr[end] = arr[end],arr[start]   #Change de position of the start and end so the first will be the last
            start +=1                #Adds up to the position in the start so now its the second position
            end -= 1                 #Decrease the end position so it will be [end-1]
        arr= ''.join(arr)            #Adds the values of the array into a new string ' '
        return(arr)
    
    else:
        while start < end:           #While the start index is lower than the end index
            arr[start],arr[end] = arr[end],arr[start]   #Change de position of the start and end so the first will be the last
            start +=1                #Adds up to the position in the start so now its the second position
            end -= 1                 #Decrease the end position so it will be [end-1]
    return arr



Array = 'word'
print(Array)
rev_array = revArr(Array,0,3)
print(rev_array)
