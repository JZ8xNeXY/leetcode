from typing import List
from collections import deque, defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        quque = deque([source])
        visited = [False] * n
        visited[source] = True

        while quque:
            node = quque.popleft()

            if node == destination:
                return True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    quque.append(neighbor)

        return False


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

solution = Solution()
print(solution.validPath(n, edges, source, destination))
