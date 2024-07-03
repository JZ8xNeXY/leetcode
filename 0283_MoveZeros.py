def moveZeroes(nums):
    nonZeroIndex = 0
    for currentIndex in range(len(nums)):
        if nums[currentIndex] != 0:
            nums[nonZeroIndex] = nums[currentIndex]
            nonZeroIndex += 1

    for i in range(nonZeroIndex, len(nums)):
        nums[i] = 0

    return nums

    # テストケース
nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))
