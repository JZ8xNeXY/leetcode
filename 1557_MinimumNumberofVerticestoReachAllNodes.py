from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [0] * n

        for _, v in edges:
            count[v] += 1

        result = []

        for i in range(n):
            if count[i] == 0:
                result.append(i)

        return result


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
solution = Solution()
print(solution.findSmallestSetOfVertices(n, edges))
