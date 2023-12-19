def kidsWithCandies(candies,extraCandies):
    lista = []
    for i in candies:
        lista.append((i+extraCandies) >= max(candies))
    return lista