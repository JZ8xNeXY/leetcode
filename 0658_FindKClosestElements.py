class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left + right) // 2

            # if x - arr[mid]:現在の部分配列の左端からxまでの距離
            # arr[mid + k] - x:次の部分配列の右端からxまでの距離
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]


arr = [1, 2, 3, 4, 5]
k = 3
x = 3

solution = Solution()
print(solution.findClosestElements(arr, k, x))
