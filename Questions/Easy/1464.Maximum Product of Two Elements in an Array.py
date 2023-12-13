class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    hash_map[i,j] = nums[i]*nums[j]
        max_value = max(hash_map.values())
        max_keys = []
        for key, value in hash_map.items():
            if value == max_value:
                max_keys.append(key)
        
        value = (nums[max_keys[0][0]]-1) * (nums[max_keys[0][1]]-1)
        return value