class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        n = len(intervals)

        intervals.sort(key=lambda x: x[1])
        non_overlap_count = 0

        end = float('-inf')

        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
                non_overlap_count += 1

        return n - non_overlap_count
