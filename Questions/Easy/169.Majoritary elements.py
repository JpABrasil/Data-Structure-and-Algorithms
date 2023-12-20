class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic = {}
        lista = []
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1 
        for j in dic:
            if dic[j] > n/2:
                return j