class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            original = x
            reversed_num = 0
            while x > 0:
                reversed_num = reversed_num * 10 + x % 10
                x //= 10

        return original == reversed_num
