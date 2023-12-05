#Brute Force
def maximumCount(nums):
    count_n = 0
    count_p = 0
    for i in range(0,len(nums)):
        if nums[i] > 0:
            count_p = count_p + 1
            print(count_p)
        if nums[i] < 0:
            count_n = count_n + 1
            print(count_n)
    if count_p >= count_n:
        return count_p
    else:
         return count_n
    
print(maximumCount([-2,-1,-1,1,2,3]))
