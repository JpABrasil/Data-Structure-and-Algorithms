def containsDuplicate(nums):
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
            break
    return False
            
        
result = containsDuplicate([1,2,3,4])
print(result)