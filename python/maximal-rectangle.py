def maximalRectangle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[[0,0] for i in cols] for j in rows]

    def recurse(i, j):
        if i <0 or j < 0:
            return [0, 0]
        if matrix[i][j] == 0:
            recurse(i - 1, j)
            recurse(i, j - 1)
        elif matrix[i][j] == 1:
            if dp[i][j] == 0:
                x1, y1= recurse(i- 1, j)
                x2, y2 = recurse(i , j - 1)
                x1 = x1 + 1
                y1 = min(y1, y2)
                y2 = y2 + 1
                x2 = min(x2, x1)
                dp[i][j] = [x2, y2] if x2 * y2 > y2 * x2 else [y2, x2]
        return dp[i][j]
    
