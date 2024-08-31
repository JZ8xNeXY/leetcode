from typing import list


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = list(set1 & set2)

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
solution = Solution()
solution.intersection(num1, num2)
