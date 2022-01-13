D = {}
def lcs(i, j):
    if i == n or b == m:
        return 0
    if (i , j) in D:
        return D[i, j]
    if a[i] == b[j]:
        D[(i,j)] = 1 + lcs(i + 1, j + 1)
    else:
        D[(i,j)] = max(lcs(i + 1, j), lcs(i , j + 1))
    return D[(i,j)]

a = input()
b = input()
n = len(a)
m = len(b)
print(lcs(0,0))