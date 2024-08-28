def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'

            if top_element != bracket_map[char]:
                return False

        else:
            stack.append(char)

    return not stack


print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
