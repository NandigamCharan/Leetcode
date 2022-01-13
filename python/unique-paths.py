class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        D = {}
        m = m - 1
        n = n - 1
        def recurse(i,j):
            if i == m:
                return 1
            if j == n:
                return 1
            if (i,j) not in D:
                D[(i,j)] =  recurse(i + 1, j) + recurse(i, j + 1)
            return D[(i,j)]
        return recurse(0,0)