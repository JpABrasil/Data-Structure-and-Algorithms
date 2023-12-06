def totalMoney(n):
    total = 0
    for i in range(n):
        if i % 7 == 0:  
            segunda= (i // 7) + 1  
        total += segunda + (i % 7)  
        print(total)

totalMoney(10)

    