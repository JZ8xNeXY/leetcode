from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        # count = Counter(s)

        # for index, char in enumerate(s):
        #     if count[char] == 1:
        #         return index

        return -1

        count = Counter(s)

        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1


# テストケース
s = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s))  # 出力: 0
