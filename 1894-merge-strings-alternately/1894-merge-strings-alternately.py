class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        while len(word1) > 0 and len(word2) > 0: 
            result = result + word1[0]
            result = result + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        if len(word1) > 0: 
            result = result + word1
        elif len(word2) > 0: 
            result = result + word2
        return result
        