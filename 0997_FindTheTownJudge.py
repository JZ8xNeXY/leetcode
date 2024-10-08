from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n+1)

        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1

        for i in range(1, n+1):
            if trust_count[i] == n-1:
                return i

        return -1


n = 3
trust = [[1, 3], [2, 3]]

solution = Solution()
print(solution.findJudge(n, trust))
