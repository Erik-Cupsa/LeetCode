class Solution(object):
    def asteroidCollision(self, asteroids):
        result = []
        for num in asteroids:
            while len(result) > 0 and num < 0 and result[-1] > 0:
                if abs(num) > result[-1]:
                    result.pop()
                elif abs(num) == result[-1]:
                    result.pop()
                    break
                else:
                    break
            else:
                result.append(num)
        return result