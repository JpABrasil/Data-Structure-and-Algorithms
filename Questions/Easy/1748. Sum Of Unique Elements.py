def sumOfUnique(nums):
    dic = {}
    lista = []
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for j in dic:
        if dic[j] == 1:
            lista.append(j)
    return(sum(lista))
sumOfUnique([1,2,3,2])
