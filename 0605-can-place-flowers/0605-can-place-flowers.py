class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        allowed = 0
        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0: 
            flowerbed[0] = 1
            allowed += 1
        if len(flowerbed) == 1 and flowerbed[0] == 0: 
            allowed += 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0: 
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0: 
                    allowed += 1
                    flowerbed[i] = 1
        if len(flowerbed) >= 2 and flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0: 
            allowed += 1
        return n <= allowed


        