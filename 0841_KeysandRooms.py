from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = [False] * n

        stack = [0]

        visited[0] = True

        while stack:
            current_room_key = stack.pop()
            for key in rooms[current_room_key]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)


rooms = [[1, 2], [2], [3], []]
solution = Solution()
print(solution.canVisitAllRooms(rooms))
