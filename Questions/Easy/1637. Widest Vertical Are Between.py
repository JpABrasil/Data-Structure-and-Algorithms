def maxWidth(points):
    arr1 = []
    for i in points:
        arr1.append(i[0])
    sort = sorted(arr1)
    arr2 = []
    for i in range(len(sort)-1):
        diff = sort[i+1] - sort[i]
        arr2.append(diff)
    print(max(arr2))
maxWidth([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])