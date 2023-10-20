class Solution(object):
    def removeElement(self, nums, val):
        right = 0
        for left in range(len(nums)):
            if nums[left] != val: 
                nums[right], nums[left] = nums[left], nums[right] 
                right += 1
        return right
        