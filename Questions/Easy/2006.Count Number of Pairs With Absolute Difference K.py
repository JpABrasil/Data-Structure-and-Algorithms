def countKDifference(nums,k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[j]-nums[i]) == k:
                count +=1
    return count