from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # リストをヒープに変換
        heapq.heapify(self.heap)

        # ヒープを作成しサイズを制限
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        print(self.heap[0])
        return self.heap[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
kthLargest.add(3)

kthLargest.add(5)

kthLargest.add(10)

kthLargest.add(9)

kthLargest.add(4)
