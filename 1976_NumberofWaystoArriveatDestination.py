from typing import List
import heapq

MOD = 10**9 + 7

# 最短距離の経路数を数える。今回なら距離7の経路数を計算する。


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # グラフの初期化 (隣接リスト)
        graph = [[] for _ in range(n)]

        for u, v, time in roads:
            graph[u].append((v, time))  # タプルで(隣接ノード, 距離)を追加
            graph[v].append((u, time))  # タプルで(隣接ノード, 距離)を追加

        print(graph)

        # 距離と経路数の初期化
        dist = [float('inf')] * n  # 全ノードの初期距離は無限大（最短距離を見つけるため）
        dist[0] = 0  # 始点(ノード0)の距離は0

        ways = [0] * n  # 各ノードへの経路数をカウントするリスト
        ways[0] = 1  # 始点にたどり着く経路は1つ

        # プライオリティキュー (ダイクストラ法で使用)
        queue = [(0, 0)]  # (ノード, 距離)のタプル。距離を優先するために距離が先

        while queue:
            # プライオリティキューから現在の最短距離のノードを取り出す
            node, current_dist = heapq.heappop(queue)

            if current_dist > dist[node]:  # 既に最短距離で訪問している場合はスキップ
                continue

            # 現在のノードから隣接するノードを確認
            for neighbor, next_dist in graph[node]:  # 隣接ノードとそのノードまでの距離
                new_dist = current_dist + next_dist  # 隣接ノードまでの新しい距離

                # 距離
                if new_dist < dist[neighbor]:  # 新しい距離が短ければ距離を更新
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]  # 新しい最短経路が見つかったので、経路数を引き継ぐ
                    # ヒープに新しい距離を追加して再計算
                    heapq.heappush(queue, (neighbor, new_dist))

                # 経路数
                elif new_dist == dist[neighbor]:  # 同じ距離の場合、経路数を加算
                    # MODで答えが大きくならないようにする
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

                print(ways)
        return ways[n-1]  # 最終的に目的地(ノードn-1)にたどり着く経路数を返す


# テストケースの実行
n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3],
         [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
solution = Solution()
print(solution.countPaths(n, roads))
