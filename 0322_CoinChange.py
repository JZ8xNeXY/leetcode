from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for index in range(1, amount+1):
            for coin in coins:
                if index >= coin:
                    dp[index] = min(dp[index], dp[index-coin]+1)
        return dp[amount] if dp[amount] != amount + 1 else -1
