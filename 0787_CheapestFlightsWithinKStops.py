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

        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]

        while heap:
            current_cost, city, transfer_cost = heapq.heappop(heap)

            if city == dst:
                return current_cost

            if transfer_cost > k:
                continue

            for neighbor, next_cost in graph[city]:
                new_cost = current_cost + next_cost

                if new_cost < dist[neighbor][transfer_cost+1]:
                    dist[neighbor][transfer_cost+1] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, transfer_cost+1))

        return -1
