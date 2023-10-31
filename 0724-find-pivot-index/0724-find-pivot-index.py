class Solution(object):
    def pivotIndex(self, nums):
        right = sum(nums)
        left = 0
        print(right)
        for i in range(len(nums)):
            left += nums[i]
            if left == right:
                return i
            else:
                right -= nums[i]
        return -1