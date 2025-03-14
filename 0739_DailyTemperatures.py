from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                preview_index = stack.pop()
                answer[preview_index] = i - preview_index

            stack.append(i)

        return answer
