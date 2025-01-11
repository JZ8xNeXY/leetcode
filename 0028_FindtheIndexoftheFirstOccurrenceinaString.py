class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1

        if len(needle) > len(haystack):
            return -1

        needle_length = len(needle)

        for index in range(len(haystack)-needle_length+1):
            if needle == haystack[index:index + needle_length]:
                return index

        return -1
