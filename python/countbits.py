class Solution:
    def countBits(self, n: int) -> List[int]:
        n = n + 1
        p = 1
        A = [0]
        for i in range(1, n):
            if i % 2 == 0:
                if i % p == 0:
                    p = i
                    A.append(1)
                else:
                    A.append(1 + A[(i % p)])
            else:
                A.append(A[-1] + 1)
        return A