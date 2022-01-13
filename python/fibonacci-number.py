class Solution:
    def fib(self, n: int, D = {}) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in D:
            D[n] = self.fib(n-1, D) + self.fib(n - 2, D)
        return D[n]