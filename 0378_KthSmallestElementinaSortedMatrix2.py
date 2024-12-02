from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        max_heap = []

        for row in matrix:
            for num in row:
                heapq.heappush(max_heap, -num)
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        return -max_heap[0]


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
solution = Solution()
print(solution.kthSmallest(matrix, k))
