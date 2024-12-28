import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # (cost, node, stops)
        heap = [(0, src, 0)]

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        while heap:
            current_cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return current_cost
            if stops > k:
                continue
            for neighbor, next_cost in graph[node]:
                new_cost = current_cost + next_cost
                if new_cost < dist[neighbor][stops+1]:
                    dist[neighbor][stops+1] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, stops+1))

        return -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

solution = Solution()
print(solution.findCheapestPrice(n, flights, src, dst, k))
