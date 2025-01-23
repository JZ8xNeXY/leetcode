from typing import List
import heapq
from collections import defaultdict

MOD = 10**9 + 7


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))

        dist = [float('inf')] * n
        dist[0] = 0

        ways = [0] * n
        ways[0] = 1

        queue = [(0, 0)]

        while queue:

            node, current_dist = heapq.heappop(queue)

            if current_dist > dist[node]:
                continue

            for neighbor, next_dist in graph[node]:
                new_dist = current_dist + next_dist

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]

                    heapq.heappush(queue, (neighbor, new_dist))

                elif new_dist == dist[neighbor]:

                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1]
