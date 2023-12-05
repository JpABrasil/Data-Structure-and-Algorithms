from collections import defaultdict
#Brute Force Approach
def twoSum(nums,target):
    result = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target and i != j:
                result.append(i)
                result.append(j)
    return result

#Hash Approach
def twosums(nums,target):
    map = {}
    #for index and number in nums
    for i,num in enumerate(nums):
        #The complement will be equal the target - the number
        complement = target-num
        #If the complement it is in the hashmap
        if complement in map:
            #Return the index of the complement and the index of the number
            return [map[complement],i]
        #Registrate the number as a key in the hashmap and atributte the index as a value
        map[num] = i
    return []

owekw = twosums([3,2,4],6)
print(owekw)