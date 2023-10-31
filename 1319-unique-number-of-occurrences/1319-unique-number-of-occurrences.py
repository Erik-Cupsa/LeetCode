class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}
        for num in arr:
            temp = dic.get(num, 0)
            temp += 1
            dic[num] = temp
        occurences = dic.values()
        result = []
        for item in occurences:
            if item in result:
                return False
            result.append(item)
        return True

        