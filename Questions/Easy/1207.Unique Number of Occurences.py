def uniqueOccurrences(arr):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1 
    values = list(dic.values())
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] == values[j]:
                return False
    return True

result = uniqueOccurrences([1,2])
print(result)