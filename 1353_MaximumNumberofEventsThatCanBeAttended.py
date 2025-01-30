import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
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

            if min_heap:
                heapq.heappop(min_heap)
                attended_events += 1
                current_day += 1

            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)

        return attended_events
