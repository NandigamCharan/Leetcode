import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        D = dict()

        for i in nums:
            if i not in D:
                D[i] = 1
            else:
                D[i] = D[i] + 1
        
        count = 0
        
        for j in D:
            count = count + math.comb(D[j], 2)
            
        return count