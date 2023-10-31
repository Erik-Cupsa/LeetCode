class Solution(object):
    def numIdenticalPairs(self, nums):
        dic = {}
        for num in nums:
            count = dic.get(num, 0)
            count += 1
            dic[num] = count
        result = 0
        for num in dic.values():
            current = (num * (num-1)) // 2
            result += current
        return result