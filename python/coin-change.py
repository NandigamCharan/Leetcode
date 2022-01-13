class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def recurse(amount):
            if amount < m:
                return float('inf')
            if amount in coins:
                return 1
            if amount in D:
                return D[amount]
            x = float('inf')
            for i in coins:
                y = recurse(amount - i)
                x = min(x, y)
            D[amount] = x + 1
            return D[amount]
        if amount == 0:
            return 0
        D = {}
        m = min(coins)
        ans = recurse(amount)
        return ans if ans != float("inf") else -1