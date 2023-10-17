class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        words = s.split(" ")
        words = words[::-1]
        result = ''
        for word in words: 
            if word.strip(): 
                result = result + " " + word.strip()
        return result.strip()
        