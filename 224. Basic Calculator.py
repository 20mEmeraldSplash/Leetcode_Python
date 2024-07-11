class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        filterS = [c for c in s if c != ' ']
        stack = []
        num = 0
        sign = 1
        result = 0

        for i in filterS:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "+":
                result += sign * num
                num = 0
                sign = 1
            elif i== "-":
                result += sign * num
                num = 0
                sign = -1
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif i == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  # sign
                result += stack.pop()  # result
        result += sign * num
        return result

  复杂度O(N)
