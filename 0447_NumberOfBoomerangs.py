from collections import defaultdict
import math


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0

        for i in points:
            distance_count = defaultdict(int)

            for j in points:
                if i == j:
                    continue

                distance = (i[0] - j[0]) ** 2 + (i[1]-j[1]) ** 2
                distance_count[distance] += 1

            for count in distance_count.values():
                result += count * (count - 1)

        return result
