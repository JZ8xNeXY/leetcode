class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char not in bracket_map:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else '#'

                if top_element != bracket_map[char]:
                    return False

        return not stack


print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
