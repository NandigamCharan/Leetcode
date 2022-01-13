class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        D = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for i in s:
            if i not in D:
                stack.append(i)
                print(1)
            elif stack == [] or stack[-1] != D[i]:
                return False
            else:
                stack.pop()
        if stack == []:
            return True
            
        