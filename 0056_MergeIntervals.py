from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            print(interval)
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
solution = Solution()
print(solution.merge(intervals))
