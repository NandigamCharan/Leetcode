def unique_paths(m, n):
    D = {}
    def recurse(i,j):
        if i == m:
            return 1
        if j == n:
            return 1
        if (i,j) not in D:
            D[(i,j)] = 2 + recurse(i + 1, j) + recurse(i, j + 1)
        return D[(i,j)]
    recurse(0,0)
