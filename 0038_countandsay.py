class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        previous_term = self.countAndSay(n - 1)
        result = ""
        i = 0

        while i < len(previous_term):
            count = 1
            while i + 1 < len(previous_term) and previous_term[i] == previous_term[i + 1]:
                count += 1
                i += 1
            result += str(count) + previous_term[i]
            i += 1

        return result


solution = Solution()
print(solution.countAndSay(5))
