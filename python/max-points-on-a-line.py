class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def number(x, y):
            infslop = 0
            D = defaultdict(int)
            for i, j in points:
                cx = i - x
                cy = j - y
                if cx == 0 and cy == 0:
                    continue
                if cy == 0:
                    infslop += 1
                else:
                    D[cx/cy] += 1
            return max(max(D.values(), default = 0), infslop)
        m = 0
        for x, y in points:
            a = number(x, y)
            m = max(a, m)
        return m + 1