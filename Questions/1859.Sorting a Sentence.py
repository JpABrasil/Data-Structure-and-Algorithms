#Using bubble sort to do this :)
def sortSentence(s):
    words = s.split()
    n = len(words)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if words[j][-1] > words[j+1][-1]:
                words[j], words[j+1] = words[j+1], words[j]
                swapped = True
        if (swapped == False):
            break
    string = ''
    for i in range(len(words)):
        words[i] =  words[i][0:len(words[i])-1]   
        string = string + words[i] + ' '
    print(string)
sortSentence('is2 a3 This1 sentece4')