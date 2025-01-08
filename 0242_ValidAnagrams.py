from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s.lower()) == Counter(t.lower())


solution = Solution()
s = "anagram"
t = "nagaram"

print(solution.isAnagram(s, t))
