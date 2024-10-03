from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
            print(dp)

        return dp[target]


nums = [1, 5, 6]

solution = Solution()
print(solution.canPartition(nums))
