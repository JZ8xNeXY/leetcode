from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains_set = set()

        for num in nums:
            if num in contains_set:
                return True
            contains_set.add(num)

        return False
