def LargestAltitude(gain):
    count = [0]
    for index,i in enumerate(gain):
        count.append(count[index] + i)
    print(max(count))
LargestAltitude([-5,1,5,0,-7])