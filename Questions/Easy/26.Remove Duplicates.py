def removeduplicates(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]== nums[j]:
                duplicate = nums[i]
    print(duplicate)
removeduplicates([1,1,2])