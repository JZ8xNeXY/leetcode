from typing import List
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        print(graph)

        def dfs(node, parent):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if not dfs(neighbor, node):  # nodeをparentとして渡す
                        return False
                elif neighbor != parent:
                    return False
            return True

        if not dfs(0, -1):
            return False

        return all(visited)


n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
solution = Solution()
print(solution.validTree(n, edges))
