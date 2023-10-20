class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        right = 0
        for left in range(n): 
            if nums[left] != 0: 
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
        return nums

        