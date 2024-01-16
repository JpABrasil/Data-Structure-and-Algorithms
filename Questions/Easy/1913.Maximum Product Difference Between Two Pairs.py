def maxProductDifference(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_arr = [sorted(nums)[0],sorted(nums)[1]]
        max_arr = [sorted(nums)[-1],sorted(nums)[-2]]
        product_diff = (max_arr[0]*max_arr[1]) - (min_arr[0]*min_arr[1])
        return product_diff
        