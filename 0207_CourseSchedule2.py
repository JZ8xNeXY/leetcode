from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)

        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        visited_count = 0
        while queue:
            current = queue.popleft()
            visited_count += 1

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_count == numCourses


numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]

solution = Solution()
print(solution.canFinish(numCourses, prerequisites))
