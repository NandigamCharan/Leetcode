class Solution:
    def tribonacci(self, n: int, D = {}) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n not in D:
            D[n] = self.tribonacci(n - 1, D) + self.tribonacci(n - 2, D) + self.tribonacci(n - 3, D)
        return D[n]