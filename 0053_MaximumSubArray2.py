from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        max_sum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

            max_sum = max(max_sum, dp[i])

        print(dp)
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
solution.maxSubArray(nums)
