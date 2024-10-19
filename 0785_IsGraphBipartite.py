from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        color = [0] * n

        for node in range(n):
            if not visited[node]:
                quque = deque([node])
                visited[node] = True
                color[node] = 1

            print(visited)

            while quque:
                current = quque.popleft()
                print(current)
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        color[neighbor] = -color[current]
                        visited[neighbor] = True
                        quque.append(neighbor)

                    elif color[neighbor] == color[current]:
                        return False
        return True


graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
solution = Solution()

print(solution.isBipartite(graph))
