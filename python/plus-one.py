class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = -(len(digits))
        c = 1
        i = -1
        while i >= n:
            s = digits[i] + c
            c = int(s / 10)
            digits[i] = s % 10
            i = i - 1
            if c == 0:
                return digits
        if c > 0:
            digits.insert(0, c)
        return digits
            
            
            