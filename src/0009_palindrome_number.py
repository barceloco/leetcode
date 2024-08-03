class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        xarray = []
        while x>0:
            xarray.append(x%10)
            x = x//10
        ispal = True
        for idx in range(len(xarray)//2):
            if xarray[idx] != xarray[len(xarray)-idx-1]:
                ispal = False
        return ispal
