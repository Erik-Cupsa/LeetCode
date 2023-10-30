class Solution(object):
    def longestOnes(self, nums, k):
        longest = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if k == 0:
                    while nums[curr] != 0:
                        curr += 1
                    curr += 1
                else:
                    k -= 1
            longest = max(longest, i-curr + 1)
        return longest
        