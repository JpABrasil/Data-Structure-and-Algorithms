def runningSum(nums):
    lista =  []
    count = 0
    for i in nums:
       count += i
       lista.append(count)
    print(lista)
runningSum([1,2,3,4])