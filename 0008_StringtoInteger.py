class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i] == ' ':
            i += 1

        while i < len(s) and s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN

        return num
