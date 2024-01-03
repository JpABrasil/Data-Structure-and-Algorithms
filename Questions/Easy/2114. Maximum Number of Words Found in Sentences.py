def maxNumberOfWords(sentences):
    lista = []
    lista2 = []
    for i in sentences:
        lista.append(i.split())
    for i in lista:
        lista2.append(len(i))
    print(max(lista2))

maxNumberOfWords(["please wait","continue to fight","continue to win"])