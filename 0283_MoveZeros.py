from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_index = 0

        for num in nums:
            if num != 0:
                nums[zero_index] = num
                zero_index += 1

        for j in range(zero_index, len(nums)):
            nums[j] = 0
