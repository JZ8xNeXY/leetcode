from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(path: List[int], used: List[bool]):
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result


nums = [1, 2, 3]
solution = Solution()
print(solution.permute(nums))
