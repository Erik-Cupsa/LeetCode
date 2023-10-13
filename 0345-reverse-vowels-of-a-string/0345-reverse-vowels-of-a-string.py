class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word = [''] * len(s)
        stack = []
        for i, letter in enumerate(s): 
            if letter in vowels: 
                stack.append(letter)
                word[i] = "***"
            else: 
                word[i] = letter
        for i, letter in enumerate(word): 
            if letter == '***': 
                word[i] = stack.pop()
        return ''.join(word)
        