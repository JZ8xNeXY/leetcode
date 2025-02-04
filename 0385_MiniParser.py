class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''

        for char in s:
            if char == '[':
                stack.append(NestedInteger())
            elif char == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                if len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)
            elif char == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:
                num += char

        return stack[0]
