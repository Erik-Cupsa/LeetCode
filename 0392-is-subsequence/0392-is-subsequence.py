class Solution(object):
    def isSubsequence(self, s, t):
        first = 0
        for letter in t: 
            if first < len(s) and s[first] == letter: 
                first += 1
        if first >= len(s): 
            return True
        return False
        