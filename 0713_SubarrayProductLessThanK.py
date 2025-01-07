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

        for right, num in enumerate(nums):
            product *= num

            while product >= k:
                product /= nums[left]
                left += 1

            count += right - left + 1

        return count
