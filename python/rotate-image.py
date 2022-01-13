class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def flip(M, s, e):
            """
            m[start][1], m[1][n], m[n][n-1], m[n-i][start]
            """
            if e - s <= 1:
                return
            n = e - 1
            for i in range(0, n - s):
                M[s][s + i], M[s + i][n], M[n][n-i], M[n-i][s] = M[n-i][s], M[s][s + i], M[s + i][n], M[n][n-i]
            flip(M, s + 1, e - 1)
        return flip(matrix, 0, len(matrix))
    