class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        A = []
        for i in range(numRows):
            x = []
            A.append(x)
        order = True
        r = 0
        for i in s:
            A[r].append(i)
            if r == 0:
                r = r + 1
                order = True
            elif r == numRows - 1:
                r = r - 1
                order = False
            else:
                if order:
                    r = r + 1
                else:
                    r = r - 1
        
        X = []
        for i in A:
            X.append("".join(i))
        return "".join(X)
                