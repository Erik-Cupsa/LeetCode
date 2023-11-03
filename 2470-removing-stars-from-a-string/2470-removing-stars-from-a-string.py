class Solution(object):
    def removeStars(self, s):
        result = []
        for letter in s:
            if letter == '*':
                result.pop()
            else:
                result.append(letter)
        result = "".join(result)
        return result
        