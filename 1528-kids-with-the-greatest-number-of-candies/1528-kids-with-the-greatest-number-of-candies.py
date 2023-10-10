class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = [None] * len(candies)
        maxArray = sorted(candies, reverse=True)
        maxVal = maxArray[0]
        for i in range(len(candies)): 
            if candies[i] + extraCandies >= maxVal: 
                result[i] = True
            else: 
                result[i] = False
        return result
        