def findWordsContaining(words,x):
    lista = []
    for s in range(len(words)):
        if x in words[s]:
            lista.append(s)
    return lista

result = findWordsContaining(["leet","code"], "e")
print(result)