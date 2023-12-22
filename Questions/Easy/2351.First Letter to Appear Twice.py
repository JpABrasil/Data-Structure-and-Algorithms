def repeatedCharacter(s):
    dic = {}
    for i in s:
        if i in dic.keys():
            return i
        else:
            dic[i] = 1