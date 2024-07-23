class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        sign = 1
        while i < len(s) and s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        num = 0
        while i < len(s) and s[i].isdigit():
            num = num*10 + int(s[i])
            i += 1

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num


solution = Solution()
print(solution.myAtoi("                  42"))
