from typing import List

# 分割統治法


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return self._longestCommonPrefix(strs, 0, len(strs)-1)

    def _longestCommonPrefix(self, strs: List[str], left: int, right: int) -> str:
        if left == right:
            return strs[left]

        mid = (left + right) // 2
        lcpLeft = self._commonPrefix(strs, left, mid)
        lcpRight = self._commonPrefix(strs, mid+1, right)

        return self._commonPrefix(lcpLeft, lcpRight)

    def _commonPrefix(self, left: str, right: str) -> str:
        minLength = min(len(left), min(right))
        for i in minLength:
            if left[i] != right[i]:
                return left[:i]

        return left[:minLength]
