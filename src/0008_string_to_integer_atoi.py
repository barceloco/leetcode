class Solution:
    def myAtoi(self, s: str) -> int:
        nbr0 = 48
        sign = 1
        i=0
        while i<len(s) and s[i] == " ":
            i += 1
        if i<len(s) and s[i] in ["+", "-"]:
            if s[i] == "-":
                sign = -1
            i += 1;
        digits=[]
        while i<len(s) and (ord(s[i])-nbr0)>=0 and (ord(s[i])-nbr0)<10:
            digits.append(ord(s[i])-nbr0)
            i+=1
        res = 0
        for d in digits:
            res = 10*res + d
        res = res * sign
        if res < -2**31:
            return -2**31
        if res > 2**31-1:
            return 2**31-1
        return int(res)