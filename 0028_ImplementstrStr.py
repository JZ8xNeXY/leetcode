class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1

        # needle_length = len(needle)
        # for i in range(len(haystack)-needle_length + 1):
        #     if haystack[i: i + needle_length] == needle:
        #         return i

        needle_length = len(needle)

        for i in range(len(haystack)-needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return i

        return -1
