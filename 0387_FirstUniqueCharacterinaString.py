from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        # frequency = Counter(s)
        # print(frequency)

        # for index, char in enumerate(s):
        #     if frequency[char] == 1:
        #         return index

        # return -1

        duplicates = set()
        position = {}

        for i, char in enumerate(s):
            if char in position:
                duplicates.add(char)
            else:
                position[char] = i

        for char in s:
            if char not in duplicates:
                return position[char]

        return -1


solution = Solution()
print(solution.firstUniqChar("leetcode"))
