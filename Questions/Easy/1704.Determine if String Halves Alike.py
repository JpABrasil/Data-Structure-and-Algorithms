def halvesAreAlike(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']     
    half_size = len(s)//2
    firsth = s[0:half_size]
    secondh = s[half_size:len(s)]
    countf = 0
    counts = 0
    for i in firsth:
        if i in vowels:
            countf +=1
    for i in secondh:
        if i in vowels:
            counts += 1
    if countf == counts:
        return True
    else:
        return False
halvesAreAlike('book')