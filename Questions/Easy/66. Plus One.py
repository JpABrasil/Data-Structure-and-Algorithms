def plusOne(digits):
    string = ""
    for i in digits:
        string += f"{i}"
    integer = int(string) + 1
    string = str(integer)
    lista = list(string)
    lista2 = []
    for j in lista:
        number = int(j)
        lista2.append(number)
    return lista2