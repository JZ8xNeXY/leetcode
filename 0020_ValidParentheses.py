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


# クラスのインスタンスを作成
solution = Solution()

# メソッドを正しく呼び出す
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([)]"))    # False
print(solution.isValid("{[]}"))    # True
