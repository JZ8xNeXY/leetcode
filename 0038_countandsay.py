class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        preview_term = self.countAndSay(n-1)
        result = ''
        index = 0

        while index < len(preview_term):
            count = 1
            while index + 1 < len(preview_term) and preview_term[index] == preview_term[index+1]:
                count += 1
                index += 1
            result += str(count) + preview_term[index]
            index += 1

        return result
