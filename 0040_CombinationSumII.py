from typing import List, Set


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results: List[List[int]] = []

        def backtrack(start: int, path: List[int], remaining: int) -> List[List[int]]:
            if remaining == 0:
                results.append(list(path))
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                backtrack(i+1, path, remaining-candidates[i])

                path.pop()

            return results

        backtrack(0, [], target)

        return results


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
solution = Solution()
print(solution.combinationSum2(candidates, target))
