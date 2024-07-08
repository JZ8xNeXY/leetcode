from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # for i in range(len(nums)):
        #     if nums[i] in count:
        #         count[nums[i]] += 1
        #     else:
        #         count[nums[i]] = 1

        # count = Counter(nums)
        # return max(count, key=count.get)

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


# テストケース
solution = Solution()
print(solution.majorityElement([3, 2, 3]))  # 出力: 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 出力: 2
