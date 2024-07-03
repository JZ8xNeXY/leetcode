import time


class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [dict[complement], index]
            dict[num] = index
        return None


nums = [2, 3, 6, 11, 15]
target = 9

# 複数回計測して平均時間を求める
total_time = 0
iterations = 1000

for _ in range(iterations):
    start_time = time.time()
    Solution().twoSum(nums, target)
    end_time = time.time()
    total_time += end_time - start_time

average_time = total_time / iterations
print(
    f"Average elapsed time over {iterations} iterations: {average_time} seconds")
