from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []
        for person in people:
            queue.insert(person[1], person)

        return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
solution = Solution()
print(solution.reconstructQueue(people))
