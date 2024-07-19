class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


solution = Solution()
print(solution.addBinary(a="11", b="1"))
