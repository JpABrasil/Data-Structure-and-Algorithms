def maximumWealth(accounts):
    lista = []
    for i in accounts:
        lista.append(sum(i))
    return max(lista)