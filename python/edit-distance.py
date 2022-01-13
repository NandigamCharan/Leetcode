class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recurse(a, b):
            if (a, b) in D:
                return D[(a, b)]
            if len(a) == 0 or len(b) == 0:
                D[(a, b)] = abs(len(b) - len(a))
            elif a[0] == b[0]:
                D[(a, b)] = recurse(a[1:], b[1:])
            else:
                D[(a, b)] = 1 + min(
                                recurse(a[1:], b[1:]),
                                recurse(a[1:], b),
                                recurse(a, b[1:])
                              )
            return D[(a, b)]
        D = {}
        return recurse(word1, word2)