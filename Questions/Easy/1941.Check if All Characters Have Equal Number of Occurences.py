def areOccurencesEqual(s):
    str_list  = list(s)
    dic = {}
    for i in str_list:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    values = list(dic.values())
    for i in range(len(values)-1):
        if values[i] != values[i+1]:
            return False
        print(values[i])
    return True
result = areOccurencesEqual("aaabb")
print(result)
