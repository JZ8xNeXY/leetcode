class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not target:
            return False

        row, col = 0, len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False


# matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
#     3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
# target = 5

matrix = [[-1, 3]]
target = 3

solution = Solution()
print(solution.searchMatrix(matrix, target))
