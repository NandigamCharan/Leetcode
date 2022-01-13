class Solution:
    def isNumber(self, s: str) -> bool:
        """
        0 False
        1 True
        2 Empty
        """
        def div(s, a):
            l = len(s)
            p = ["", ""]
            for i in range(l):
                if s[i] == a:
                    p[0] = s[:i]
                    p[1] = s[i + 1:]
                    return p
            p[0] = s
            return p
        
        def isNum(s):
            A = {str(x) for x in range(0,10)}
            if s == "":
                return 2
            for i in s:
                if i not in A:
                    return 0
            return 1
            
        def isInt(s):
            if s == "":
                return 2
            if s[0] == "+" or s[0] == "-":
                return isNum(s[1:])
            else:
                return 0
        
        def isFloat(s):
            p = div(s, ".")

            a = isInt(p[0])
            b = isNum(p[0])
            c = isNum(p[1])
            if ((a == 2 or b == 2) and c == 2):
                return False
            elif (a >= 1 or b >= 1) and  c >= 1:
                return True
            else:
                return False
            
        def ise(s, a):
            e = div(s, a) 
            a = isNum(e[0])
            b = isInt(e[0])
            c = isFloat(e[0])
            d = isNum(e[1])
            e = isInt(e[1])
            
            if (a == 1 or b == 1 or c) and (d == 1 or e ==1):
                return True
            else:
                return False
        def isE(s):
            if ise(s, "e") or ise(s, "E"):
                return True
            else:
                return False
        
        print(isNum(s))
        
        if isE(s) or isFloat(s) or (isInt(s) == 1) or (isNum(s) == 1):
            return True
        else:
            return False   
    