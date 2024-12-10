class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1

            count += right - left + 1

        return count


nums = [10, 5, 2, 6]
k = 100
solution = Solution()
print(solution.numSubarrayProductLessThanK(nums, k))
