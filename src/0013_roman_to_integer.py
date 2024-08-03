class Solution:
    def romanToInt(self, s: str) -> int:
        r2b= {
            "M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1
        }
        spec = {
            "IV": 4, "IX": 9, "XL": 40, "XC":90, "CD": 400, "CM":900
        }
        idx = 0;
        res = 0
        while idx < len(s)-1:
            if s[idx:idx+2] in spec.keys():
                # print(idx, s[idx:idx+2])
                res = res + spec[s[idx:idx+2]]
                idx += 2
            else:
                # print(idx, s[idx:idx+1])
                res = res + r2b[s[idx:idx+1]]
                idx += 1
        if idx<len(s):
            res = res + r2b[s[idx:idx+1]]
        return res
