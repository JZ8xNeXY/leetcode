from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)

        for _ in range(k-1):
            val, row, col = heapq.heappop(heap)

            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))

        return heapq.heappop(heap)[0]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 3
solution = Solution()
print(solution.kthSmallest(matrix, k))
