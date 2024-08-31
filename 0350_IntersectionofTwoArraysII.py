from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        count_nums1 = Counter(nums1)

        for num in nums2:
            if count_nums1[num] > 0:
                result.append(num)
                count_nums1[num] -= 1

        print(result)
        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
solution.intersect(nums1, nums2)
