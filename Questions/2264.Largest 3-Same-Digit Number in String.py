def largestGoodInteger(self, num):
    """
    :type num: str
    :rtype: str
    """
    listanumero = list(num)
    listanumeroseguidos = []
    listadaslistas = []
    lis_ta = []
    lesta = []
    for x in range(len(listanumero) - 2):
        if listanumero[x] == listanumero[x+1] == listanumero[x+2]:
            listanumeroseguidos = []
            listanumeroseguidos.append(listanumero[x])
            listanumeroseguidos.append(listanumero[x+1])
            listanumeroseguidos.append(listanumero[x+2])
            listadaslistas.append(listanumeroseguidos)
    for i in range(len(listadaslistas)):
        if len(listadaslistas[i]) !=3 :
            listadaslistas.pop(listadaslistas[i])

    for i in (listadaslistas):
        lan = ""
        for j in i:
            lan = lan +j
            lis_ta.append(lan) 
    for i in lis_ta:
        lesta.append(int(i))
    if len(lesta) != 0: 
        maiorvalor = max(lesta)
        if maiorvalor == 0:
            return "000"

    else:
        maiorvalor = ''
    return str(maiorvalor)    