from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return self._longestCommonPrefix(strs, 0, len(strs) - 1)

    def _longestCommonPrefix(self, strs: List[str], left: int, right: int) -> str:
        if left == right:
            return strs[left]

        mid = (left + right) // 2

        left_str = self._longestCommonPrefix(strs, left, mid)
        right_str = self._longestCommonPrefix(strs, mid+1, right)

        return self._commonPrefix(left_str, right_str)

    def _commonPrefix(self, left: str, right: str) -> str:
        min_length = min(len(left), len(right))

        for index in range(min_length):
            if left[index] != right[index]:
                return left[:index]

        return left[:min_length]
