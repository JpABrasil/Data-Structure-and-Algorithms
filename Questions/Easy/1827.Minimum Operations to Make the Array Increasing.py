def minOperations(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            pass
        else:
            while nums[i] >= nums[i+1]:
                nums[i+1] += 1
                count += 1
    return count
result = minOperations([1,5,2,4,1])
print(result)