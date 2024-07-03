def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1

    for i in range(k, len(nums)):
        nums[i] = None

    return k


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates(nums))
