def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
     """
    n = len(nums)
    k = k % n

    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)
