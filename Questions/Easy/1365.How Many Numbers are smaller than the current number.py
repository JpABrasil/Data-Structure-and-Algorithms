def smallerNumbersThanCurrent(nums):
        smaller_nums = []
        n = len(nums)
        for i in range(n):
            count = 0
            swapped = False
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1], nums[j]
                    count +=1
                    swapped = True
            smaller_nums.append(count)
            if (swapped == False):
                break

        return(smaller_nums) 