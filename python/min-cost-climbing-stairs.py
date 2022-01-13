class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        D = {}
        n = len(cost)
        def recurse(i):
            if i in D:
                return D[i]
            if i >= n - 2:
                return cost[i]
            else:
                D[i] = cost[i] + min(recurse(i + 2), recurse(i + 1))
            return D[i]
        return min(recurse(0), recurse(1))