from collections import defaultdict, deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1:
            return [0]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque([node for node in graph if len(
            graph[node]) == 1])  # 葉ノードをキューに追加

        remaining_nodes = n  # 残りのノード数を管理

        while remaining_nodes > 2:
            leaves_count = len(leaves)  # 葉ノードの数
            remaining_nodes -= leaves_count  # 残りのノード数を更新

            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)

        return list(leaves)


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
solution = Solution()
print(solution.findMinHeightTrees(n, edges))
