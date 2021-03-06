class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n):
            if n % 2:
                count += 1
            n >>= 1
        return count