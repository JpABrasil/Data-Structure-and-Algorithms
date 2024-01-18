def  findCenter(edges):
    first_number = edges[0][0]
    second_number = edges[0][1]
    count1= 0
    count2= 0
    for i in edges:
        if first_number in i:
            count1 += 1
        if second_number in i:
            count2 +=1
    if count1 > count2:
        return first_number
    if count2 >count1:
        return second_number
result = findCenter([[1,2],[2,3],[4,2]])
print(result)