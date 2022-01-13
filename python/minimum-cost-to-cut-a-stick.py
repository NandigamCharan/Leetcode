class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        D = {}
        def recurse(x, y):
            if (x, y) in D:
                return D[(x, y)]
            if y - x <= 1:
                return 0
            k = y - x
            ans = float("inf")
            for i in cuts:
                if i > x and i < y:
                    ans = min(ans, k +recurse(x, i) + recurse(i, y))
            D[x, y] = 0 if ans == float("inf") else ans
            return D[(x, y)]
        return recurse(0, n)