class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
