def getConcatenation(nums):
    new_array = []
    for i in range(len(nums)):
        new_array.append(nums[i])
    for j in range(len(nums)):
        new_array.append(nums[j])    
    return new_array