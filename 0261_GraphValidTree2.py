from typing import List
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        visited[0] = True

        queue = deque([(0, -1)])

        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                else:
                    if neighbor != parent:
                        return False

        return all(visited)
