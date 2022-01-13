class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        a = len(v1)
        b = len(v2)
        n = max(a, b)
        i = 0
        while i < n:
            x = 0 if i >= a else int(v1[i])
            y = 0 if i >= b else int(v2[i])
            if x > y:
                return 1
            if x < y:
                return -1
            i += 1
        return 0