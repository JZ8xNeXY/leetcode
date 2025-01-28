from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(
            row: int,
            cols: Set[int],
            diagonals: Set[int],
            anti_diagonals: Set[int],
            state: List[List[str]]
        ) -> None:
            if row == n:
                board = []
                for r in state:
                    board.append(''.join(r))
                result.append(board)
                return

            for col in range(n):
                current_diag = row - col
                current_anti_diag = row + col

                if col in cols or current_diag in diagonals or current_anti_diag in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(current_diag)
                anti_diagonals.add(current_anti_diag)
                state[row][col] = 'Q'

                backtrack(row+1, cols, diagonals, anti_diagonals, state)

                cols.remove(col)
                diagonals.remove(current_diag)
                anti_diagonals.remove(current_anti_diag)
                state[row][col] = '.'

        result: List[List[str]] = []
        state: List[List[str]] = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), state)
        return result
