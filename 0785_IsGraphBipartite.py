from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        color = [0] * n

        for node in range(n):
            if not visited[node]:
                queue = deque([node])
                visited[node] = True
                color[node] = 1
                queue = deque([node])

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        color[neighbor] = -color[current]
                        visited[neighbor] = True
                        queue.append(neighbor)

                    elif color[neighbor] == color[current]:
                        return False
        return True
