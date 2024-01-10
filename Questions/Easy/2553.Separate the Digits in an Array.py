def separateDigits(self, nums):
    arr = []
    for i in range(len(nums)):
        nums[i] =list(str(nums[i]))
    for i in nums:
        for j in i:
            arr.append(int(j))
    return arr