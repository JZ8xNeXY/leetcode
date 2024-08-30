from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()

            next_greater[num] = stack[-1] if stack else -1

            stack.append(num)

        print([next_greater[num] for num in nums1])
        return [next_greater[num] for num in nums1]


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
solution = Solution()
solution.nextGreaterElement(nums1, nums2)
