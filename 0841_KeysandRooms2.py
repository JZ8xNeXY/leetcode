from typing import List
from collections import deque


# 幅優先（BFS)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # n = len(rooms)

        # visited = [False] * n

        # quque = deque([0])

        # visited[0] = True

        # while quque:
        #     current_room_key = quque.popleft()
        #     for key in rooms[current_room_key]:
        #         if not visited[key]:
        #             visited[key] = True

        #             quque.append(key)

        # return all(visited)

        n = len(rooms)

        visited = [False] * n

        quque = deque([0])

        visited[0] = True

        while quque:
            current_room_key = quque.popleft()
            for key in rooms[current_room_key]:
                if not visited[key]:
                    visited[key] = True
                    quque.append(key)

        return all(visited)


rooms = [[1, 2, 3], [2], [3], []]
solution = Solution()
print(solution.canVisitAllRooms(rooms))
