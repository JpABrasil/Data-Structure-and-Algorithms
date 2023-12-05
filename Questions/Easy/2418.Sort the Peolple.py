#bubbleSort applied to two arrays indexed 
def sortPeople(names,heights):
    n = len(heights)       
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if heights[j] < heights[j+1]:
                names[j],names[j+1] = names[j+1], names[j]
                heights[j],heights[j+1] = heights[j+1],heights[j]
                swapped = True
        if (swapped == False):
            break
    return names
#Testing
result = sortPeople(['Mary','Jonh','Julia'],[155,190,170])
print(result)