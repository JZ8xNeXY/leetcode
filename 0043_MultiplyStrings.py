class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1
                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        result_str = ''.join(map(str, result))
        result_str = result_str.lstrip('0')

        return result_str if result_str else '0'


num1 = '2'
num2 = '3'
solution = Solution()
print(solution.multiply(num1, num2))
