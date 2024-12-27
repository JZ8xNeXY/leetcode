import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        min_heap = []
        event_index = 0
        attended_events = 0
        current_day = 0

        while event_index < len(events) or min_heap:
            if not min_heap:
                current_day = events[event_index][0]

            while event_index < len(events) and events[event_index][0] == current_day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            heapq.heappop(min_heap)
            attended_events += 1
            current_day += 1

            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)

        return attended_events


events = [[1, 2], [2, 3], [3, 4]]
solution = Solution()
print(solution.maxEvents(events))
