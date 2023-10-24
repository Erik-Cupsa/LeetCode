class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        area = 0
        while left < right: 
            currL = height[left]
            currR = height[right]
            temp = min(currL, currR) * (abs(right-left))
            area = max(area, temp)
            if currL < currR: 
                left += 1
            else: 
                right -= 1
        return area