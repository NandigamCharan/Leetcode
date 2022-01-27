def isum(S, K):
    ans = 0
    for i in range(K):
        ans = (ans << 1) + int(S[i])
    return ans

def sumBinary(N, K, S):
    def hasher(ans, old, new):
        ans = ((ans << 1) + mod - (old << K) + new)
        return ans
    mod = 10**9 + 7
    h = isum(S, K)
    ans = h
    for i in range(K, N):
        h =  hasher(h, int(S[i - K - 1]), int(S[i]))
        ans = (ans + h) % mod
    return ans

    

s = "010000000000000000000000000000000000000000000000000000000010110101010010101010000010"
k = 2
print(sumBinary(len(s), k, s))