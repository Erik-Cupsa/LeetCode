class Solution(object):
    def findMaxAverage(self, nums, k):
        s =  sum(nums[0:k])
        avg = s/float(k)

        for i in range(k, len(nums)): 
            s = s + nums[i] - nums[i-k]
            avg = max(avg, s/float(k))
        return avg