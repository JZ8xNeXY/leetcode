from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)

        for truster, trustee in trust:
            count[truster] -= 1
            count[trustee] += 1

        for i in range(n+1):
            if count[i] == n - 1:
                return i
        return -1
