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

        print(graph)  # {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]})

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


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
solution = Solution()
print(solution.validTree(n, edges))
