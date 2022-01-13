class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def recurse(x,y):
            if (x, y) in D:
                return D[(x,y)]
            if x == m and y == n:
                return grid[m][n]
            elif x == m:
                D[(x,y)] = grid[x][y] + recurse(x, y + 1)
            elif y == n:
                D[(x,y)] = grid[x][y] + recurse(x + 1, y)
            else:
                D[(x,y)] = grid[x][y] + min(recurse(x + 1, y), recurse(x, y + 1))
            return D[(x,y)]
        D = {}
        m = len(grid) - 1
        n = len(grid[0]) - 1
        return recurse(0,0)