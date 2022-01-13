class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        D = {}
        for d in nums:
            if d not in D:
                D[d] = 0
            D[d] += 1
        
        Ans = set()
        for i in D:
            D[i] = D[i] - 1
            for j in D:
                if D[j] > 0:
                    D[j] = D[j] - 1
                    c = -i - j
                    if c in D and D[c] > 0:
                        ans = [i, j, c]
                        ans.sort()
                        ans = tuple(ans)
                        Ans.add(ans)
                    D[j] = D[j] + 1
            D[i] = D[i] + 1    
        return Ans