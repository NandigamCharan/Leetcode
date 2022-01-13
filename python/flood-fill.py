class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def recurse(i,j):
            if (i, j) not in D and i >= 0 and i < m and j >= 0 and j < n:
                if image[i][j] == color:
                    D.add((i,j))
                    image[i][j] = newColor
                    recurse(i + 1, j)
                    recurse(i - 1, j)
                    recurse(i, j + 1)
                    recurse(i, j - 1)
        color = image[sr][sc]
        D = set()
        m = len(image)
        n = len(image[0])
        recurse(sr, sc)
        return image