class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "leetcode"
needle = "leet"
solution = Solution()
print(solution.strStr(haystack, needle))
