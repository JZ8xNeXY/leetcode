class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        print(costs)
        n = len(costs) // 2
        return sum(costs[i][0] for i in range(n)) + sum(costs[i][1] for i in range(n, 2*n))


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
solution = Solution()
print(solution.twoCitySchedCost(costs))
