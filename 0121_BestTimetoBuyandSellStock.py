from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if min_price > price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# テストケース
prices = [7, 1, 5, 3, 6, 4, 10]

solution = Solution().maxProfit(prices)
print(solution)
