class Solution(object):
    def decodeString(self, s):
        stack = []
        result = ""
        for l in s:
            if l == "]":
                curr = stack.pop()
                temp = ""
                while curr != "[":
                    temp = curr + temp
                    curr = stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    curr = stack.pop()
                    num = curr + num
                temp = temp * int(num)
                stack.append(temp)
            else:
                stack.append(l)
        while stack:
            result = result + stack.pop(0)
        return result
        