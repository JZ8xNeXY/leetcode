from typing import List
import heapq
from collections import defaultdict

MOD = 10**9 + 7

# 最短距離の経路数を数える。今回なら距離7の経路数を計算する。


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

                # 距離の管理
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]

                    heapq.heappush(queue, (neighbor, new_dist))

                # 経路数の管理
                elif new_dist == dist[neighbor]:

                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1]


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
solution = Solution()
print(solution.countPaths(n, roads))
