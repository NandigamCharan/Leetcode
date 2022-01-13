class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def isequal(a, b, start):
            j = start
            for i in range(0, k):
                if a[j] != b[i]:
                    return False
                j += 1
            return True

        def hasher(a):
            h = 0
            i = 0
            while i < k:
                h = (((h + prime) * basenum) + ord(a[i]))% prime
                i += 1
            return (h + prime) % prime

        def offsetof(k):
            k = k - 1
            off = 1
            for i in range(k):
                off = (off * basenum)% prime
            return off

        def rhash(h, old, new):
            return ((h + prime - ord(old) * offset) * basenum + ord(new)) % prime

        def stringmatch(a,b):

            global k; k = len(b)    # These are global variables
            global n; n = len(a)
            global prime; prime = 109
            global basenum; basenum = 256
            global offset; offset = offsetof(k)  
            bhash = hasher(b)
            h = hasher(a)
            breaker = n - k
            for i in range(n):
                if h == bhash and isequal(a, b, i):
                        return i
                if i == breaker:
                    break
                h = rhash(h, a[i], a[i + k])
            return -1
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0
        return stringmatch(haystack, needle)