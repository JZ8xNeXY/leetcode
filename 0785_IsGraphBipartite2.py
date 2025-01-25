from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        def dfs(node, current_color):
            color[node] = current_color
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    if not dfs(neighbor, -current_color):
                        return False
                elif color[neighbor] == current_color:
                    return False
            return True

        for node in range(n):
            if color[node] == 0:
                if not dfs(node, 1):
                    return False

        return True
