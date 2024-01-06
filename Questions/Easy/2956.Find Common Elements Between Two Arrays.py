def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = 0
        count2 = 0
        arr = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                count1 +=1
        arr.append(count1)
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                count2 +=1
        arr.append(count2)
        return arr