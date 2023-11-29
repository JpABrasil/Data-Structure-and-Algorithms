def binarySearch(array,columns):
    low = 0
    high = columns - 1
    while low<= high:
        mid = (low+high)//2
        if array[mid] < 0:
            high = mid-1
        else:
            low = mid+1
    return(columns-low)

def countNegatives(grid):
    rows = len(grid)
    columns = len(grid[0])
    count = 0
    for i in range(rows):
        count = count + binarySearch(grid[i],columns)

print(countNegatives())
    