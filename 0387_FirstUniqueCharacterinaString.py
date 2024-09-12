class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        # duplicate = set()
        # position = {}

        # for index, char in enumerate(s):
        #     if char not in position:
        #         position[char] = index
        #     else:
        #         duplicate.add(char)

        # for char in s:
        #     if char not in duplicate:
        #         return position[char]

        # return -1
        duplicate = set()
        position = {}

        for index, char in enumerate(s):
            if char not in position:
                position[char] = index
            else:
                duplicate.add(char)

        for char in s:
            if char not in duplicate:
                return position[char]

        return -1


s = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s))
