from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses

        def has_cycle(course):
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False

            visited[course] = 1

            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True

            visited[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True
