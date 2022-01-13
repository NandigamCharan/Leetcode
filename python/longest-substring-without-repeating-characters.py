class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        alpha = {s[0] : 0}
        m = 1
        prev = 1
        n = len(s)
        
        for i in range(1, n):
            if s[i] in alpha:
                prev = min(i - alpha[s[i]], prev + 1)
            else:
                prev += 1
            m = max(prev, m)
            print(prev)
            alpha[s[i]] = i
        return m