class Solution:
    def reverse(self, x: int) -> int:
        int_arr = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while (x>0):
            int_arr.append(x%10)
            x = x//10
        res = 0
        for ix in int_arr:
            res = 10 * res + ix
        if (res< -2**31) or (res> 2**31-1):
            return 0        
        return sign * res
