from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        index = 1

        for i, num in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = num
                index += 1

        for i in range(index, len(nums)):
            nums[index] = None
