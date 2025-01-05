from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        index = 0

        for _, num in enumerate(nums):
            if num != 0:
                nums[index] = num
                index += 1

        for _ in range(index, len(nums)):
            nums[index] = 0
            index += 1
