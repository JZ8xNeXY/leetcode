from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 0:
            return 0

        dp = [0] * len(prices)

        min_price = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_price)

            min_price = min(min_price, prices[i])

        return dp[-1]


prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
solution.maxProfit(prices)
