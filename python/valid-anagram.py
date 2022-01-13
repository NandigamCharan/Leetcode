class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        H = {}
        for i in s:
            if i not in H:
                H[i] = 1
            else:
                H[i] += 1
        for i in t:
            if i not in H:
                return False
            if H[i] == 0:
                return False
            H[i] -= 1
        for i in H:
            if H[i] > 0:
                return False
        return True
            