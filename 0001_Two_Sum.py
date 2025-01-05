class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], index]
            else:
                num_dict[num] = index

        return []
