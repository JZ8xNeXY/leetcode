from typing import List


# 深さ優先（DFS)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = [False] * n
        visited[0] = True

        queue = deque([0])

        while queue:
            current_room_key = queue.popleft()
            for neighbor in rooms[current_room_key]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return all(visited)
