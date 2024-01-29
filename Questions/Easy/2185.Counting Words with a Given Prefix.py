def prefixCount(self, words, pref):
    count = 0
    pref_len = len(pref)
    for i in words:
        i = i[0:pref_len]
        if  pref in i:
            count +=1  
    return count