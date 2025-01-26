from typing import List
from collections import deque, defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(edges)
        visited = [False] * n
        queue = deque([source])

        while queue:
            current_node = queue.popleft()

            if current_node == destination:
                return True

            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False
