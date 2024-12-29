class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(s):
            return s == s[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    path.pop()

        backtrack(0, [])
        return result


solution = Solution()
print(solution.partition("aab"))
