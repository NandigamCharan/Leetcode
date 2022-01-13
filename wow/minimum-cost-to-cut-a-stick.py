# This is rejected
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = set(cuts)
        D = {}
        def recurse(x, y):
            if (x, y) in D:
                return D[(x, y)]
            if y - x == 1:
                return 0
            k = y - x
            ans = float("inf")
            for i in range(x + 1, y): # --> here I'm going through all numbers  🤦‍♂️
                if i in cuts:         # --> and checking if it exisits in cuts
                    ans = min(ans, k +recurse(x, i) + recurse(i , y))
            D[x, y] = 0 if ans == float("inf") else ans
            return D[(x, y)]
        ans = recurse(0, n)
        return ans

# This is accepeted
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
            for i in cuts:           # --> We should sort the cuts and check if it is in the range... 😂
                if i > x and i < y:
                    ans = min(ans, k +recurse(x, i) + recurse(i, y))
            D[x, y] = 0 if ans == float("inf") else ans
            return D[(x, y)]
        ans = recurse(0, n)
        return ans

"""
## Take Aways:

for a breif moment I thought about it... not for solution but for analysis...
I ignored because I thought like 'there exists atmost n - 2 cuts, so cuts = O(n)'...
Then concluded doesn't matter what we do traversal with... 

So, always look at constraints after understanding question.

and most importantly, **Leet code** is a fucking troll...

Not only that, even if it O(n), think about it... which better for design, length of the rod is always O(n) by definition... 
But no of cuts can be lower... so looping through cuts is better...
"""