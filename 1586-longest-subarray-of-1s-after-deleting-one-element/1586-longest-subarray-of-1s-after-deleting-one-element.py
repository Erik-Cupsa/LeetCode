class Solution(object):
    def longestSubarray(self, nums):
        longest = 0
        curr = 0
        k = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[curr] == 1:
                        curr += 1
                    curr += 1
                else: 
                    k -= 1
            longest = max(longest, i - curr + 1)
        return longest - 1