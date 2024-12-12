class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                min_length = min(min_length, right-left+1)

                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]

solution = Solution()
print(solution.minSubArrayLen(target, nums))

target = 11
nums = [1, 1, 1, 1, 1, 1]

solution = Solution()
print(solution.minSubArrayLen(target, nums))
