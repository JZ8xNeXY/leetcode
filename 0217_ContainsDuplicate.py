from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains_set = set()

        for num in nums:
            if num in contains_set:
                return True
            contains_set.add(num)

        return False


solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # 出力: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # 出力: False
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # 出力: True
