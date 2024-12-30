

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 1 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        dp = [float('inf')] * n
        for end in range(n):
            if is_palindrome[0][end]:
                dp[end] = 0
            else:
                for start in range(end):
                    if is_palindrome[start + 1][end]:
                        dp[end] = min(dp[end], dp[start] + 1)

        return dp[-1]


solution = Solution()
print(solution.minCut("aab"))
