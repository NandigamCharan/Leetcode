class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        def Reverse(x):
            a = 0
            while x > 0:
                m = x%10
                a = a*10 + m
                x = int(x/10)
            return a
        
        return x == Reverse(x)
        