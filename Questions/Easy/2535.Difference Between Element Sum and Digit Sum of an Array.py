def differenceOfSum(nums):
    element_sum = sum(nums)
    arr = []
    for i in range(len(nums)):
        nums[i] = list(str(nums[i]))
    for i in nums:
        for j in i:
            arr.append(int(j))
    digit_sum = sum(arr)
    return element_sum - digit_sum    
differenceOfSum([1,15,6,3])