class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        curr = count
        for i in range(k, len(s)):
            if s[i-k] in vowels: 
                curr -= 1
            if s[i] in vowels:
                curr += 1
            count = max(count, curr)
        return count


        