from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return None

        max_num = current_num = nums[0]

        for num in nums[1:]:
            current_num = max(num, current_num + num)

            if current_num > max_num:
                max_num = current_num

        return max_num
