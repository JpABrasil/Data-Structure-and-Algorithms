def isAcronym(words,s):
    string = ""
    for i in words:
        string += i[0]
    if string == s:
        return True
    else:
        return False