class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_string = ''
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append((num, current_string))
                num = 0
                current_string = ''
            elif char == ']':
                top_num, prev_string = stack.pop()
                current_string = prev_string + current_string * top_num

            else:
                current_string += char

        return current_string


s = "3[a]2[bc]"
solution = Solution()
print(solution.decodeString(s))
