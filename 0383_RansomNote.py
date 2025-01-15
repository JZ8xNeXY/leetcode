from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False

        return True


ransomNote = "aa"
magazine = "ab"
soluiton = Solution()
print(soluiton.canConstruct(ransomNote, magazine))
