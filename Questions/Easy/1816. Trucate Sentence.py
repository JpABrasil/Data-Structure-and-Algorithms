def trucateSentece(s,k):
    splited = s.split()
    string  = ""
    for i in range(k):
        string += splited[i]
        if i < k -1:
            string += " "
    return string