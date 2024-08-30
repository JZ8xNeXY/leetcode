from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        ツーポインター法で回答する
        '''
        left, right = 0, len(numbers)-1

        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left+1, right+1]
            elif result > target:
                right -= 1
            else:
                left += 1


numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
solution.twoSum(numbers, target)
