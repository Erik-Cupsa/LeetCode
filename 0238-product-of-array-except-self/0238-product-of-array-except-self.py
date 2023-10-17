class Solution(object):
    def productExceptSelf(self, nums):
        curr = 1
        left = []
        for num in nums: 
            left.append(curr)
            curr *= num
        curr = 1
        right = []
        for num in nums[::-1]: 
            right.append(curr)
            curr *= num
        right = right[::-1]
        result = []
        for i in range(len(nums)): 
            result.append(left[i] * right[i])
        return result

                