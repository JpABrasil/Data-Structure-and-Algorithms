def countPoints(rings):
    dic = {}
    count = 0
    for i in range(len(rings)):
        if i % 2 == 0:
            if rings[i+1] in dic:
                dic[rings[i+1]] += rings[i]
            else:
                dic[rings[i+1]] = rings[i]
   
    for key,value in dic.items():
        if all(element in sorted(value) for element in['B','G','R']):
            count +=1
    return count
            
    

result = countPoints("B0B6G0R6R0R6G9")   
print(result)
