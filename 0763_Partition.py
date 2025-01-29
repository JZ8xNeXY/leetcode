from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_position = {}
        for index, char in enumerate(s):
            last_position[char] = index

        partions = []
        start, end = 0, 0

        for index, char in enumerate(s):
            end = max(end, last_position[char])
            if index == end:
                partions.append(end - start + 1)
                start = index + 1
        return partions
