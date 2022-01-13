class Solution:
    def climbStairs(self, n: int) -> int:
        def recurse(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in D:
                return D[n]
            D[n] = recurse(n - 2) + recurse(n - 1)
            return D[n]
        D = {}
        return recurse(n)