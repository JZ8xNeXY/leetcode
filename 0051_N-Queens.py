from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(
            row: int,  # 行
            cols: Set[int],  # 列
            diagonals: Set[int],  # 対角線
            anti_diagonals: Set[int],  # 反対対角線
            state: List[List[str]]  # 盤面状態２次元リスト
        ) -> None:
            # クイーンを配置できたら結果を追加
            if row == n:
                board = []
                for r in state:
                    board.append(''.join(r))
                result.append(board)
                return

            for col in range(n):
                current_diag = row - col  # 現在の位置からの対角線
                current_anti_diag = row + col  # 現在の位置からの反対の対角線

                # 衝突がないかどうか確認（列方向　対角線　反対の対角線）
                if col in cols or current_diag in diagonals or current_anti_diag in anti_diagonals:
                    continue

                # 進む　クイーンを配置
                cols.add(col)
                diagonals.add(current_diag)
                anti_diagonals.add(current_anti_diag)
                state[row][col] = 'Q'

                # 次の行を探索
                backtrack(row+1, cols, diagonals, anti_diagonals, state)

                # 戻る　クイーンを除く
                cols.remove(col)
                diagonals.remove(current_diag)
                anti_diagonals.remove(current_anti_diag)
                state[row][col] = '.'

        result: List[List[str]] = []
        state: List[List[str]] = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), state)
        return result


solution = Solution()
print(solution.solveNQueens(4))
