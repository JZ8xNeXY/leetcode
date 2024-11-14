from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        max_length = 1
        current_length = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        max_length = max(max_length, current_length)
        return max_length


nums = [100, 4, 200, 1, 3, 2]
solution = Solution()
print(solution.longestConsecutive(nums))
