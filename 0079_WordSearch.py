from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(r, c, index):
            if index == len(word):
                return True

            if (r < 0 or r >= rows) or (c < 0 or c >= cols) or visited[r][c] or board[r][c] != word[index]:
                return False

            visited[r][c] = True

            res = (backtrack(r+1, c, index+1) or
                   backtrack(r-1, c, index+1) or
                   backtrack(r, c+1, index+1) or
                   backtrack(r, c-1, index+1))

            visited[r][c] = False

            return res

        # 各セルから探索を開始
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
solution = Solution()
print(solution.exist(board, word))
