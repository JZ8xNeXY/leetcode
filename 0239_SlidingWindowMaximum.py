from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 0:
            return []

        deq = deque()
        result = []

        n = len(nums)

        for index in range(n):
            if deq and deq[0] < index - k + 1:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[index]:
                deq.pop()

            deq.append(index)

            if index >= k - 1:
                result.append(nums[deq[0]])

        return result
