from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)

        print(list(anagrams.values()))
        return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
solution.groupAnagrams(strs)
