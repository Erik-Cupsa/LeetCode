class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3: 
            return False
        curr = nums[0]
        count = 1
        maxVal = max(nums)
        maxFound = False
        for i in range(1, len(nums)): 
            if nums[i] > curr:
                count += 1
                if count == 3: 
                    return True
                if nums[i] == maxVal: 
                    count = 1
                    maxFound = True
            if not maxFound: 
                curr = nums[i]
            else: 
                maxFound = False
        return False
        