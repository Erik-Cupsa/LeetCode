class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        dic1 = {}
        dic2 = {}
        for word in word1:
            count = dic1.get(word, 0)
            count += 1
            dic1[word] = count
        for word in word2:
            count = dic2.get(word, 0)
            count += 1
            dic2[word] = count
        if sorted(dic1.keys()) == sorted(dic2.keys()) and sorted(dic1.values()) == sorted(dic2.values()):
            return True
        return False