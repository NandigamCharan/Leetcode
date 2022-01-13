class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        S = {}
        for i in strs:
            x = list(i)
            x.sort()
            x = tuple(x)

            if x not in S:
                S[x] = []
            S[x].append(i)        
        return S.values()