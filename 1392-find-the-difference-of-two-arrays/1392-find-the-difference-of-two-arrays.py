class Solution(object):
    def findDifference(self, nums1, nums2):
        result = []
        notIn1 = []
        notIn2 = []
        for num in nums1:
            if num not in nums2:
                notIn2.append(num)
        for num in nums2:
            if num not in nums1:
                notIn1.append(num)
        result.append(set(notIn2))
        result.append(set(notIn1))
        return result
        