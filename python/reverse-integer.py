class Solution:
    def reverse(self, x: int) -> int:

        ans = 0
        mul = 1
        if x < 0:
            mul = -1
            x = abs(x)
        while  0 != x:
            ans = (10 * ans) +  (x % 10)
            x = x // 10
        n = 2 ** 31
        if ans > n - 1 or ans < -n:
            return 0
        return ans * mul