from typing import List


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.BIT = [0] * (size + 1)

    def update(self, index, val):
        index += 1
        while index <= self.size:
            self.BIT[index] += val
            index += index & -index

    def sum(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self.BIT[index]
            index -= index & -index

        return result

    def sumRange(self, left, right):
        return self.sum(right) - self.sum(left-1)


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.fenwick_tree = FenwickTree(len(nums))

        for i, val in enumerate(nums):
            self.fenwick_tree.update(i, val)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.fenwick_tree.update(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.fenwick_tree.sumRange(left, right)
