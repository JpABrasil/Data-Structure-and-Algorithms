
def strStr(haystack,needle):
    splited = haystack.split(needle)
    for i in range(len(splited)):
        if splited[i] == '':
            return i
        