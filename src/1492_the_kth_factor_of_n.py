class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ath=0
        i = 0
        for i in range(1, n+1):
            if (n%i==0):
                k-=1
            if k==0:
                break
        if k==0:
            return i
        else:
            return -1

        #slower:
        while ath<k:
            i += 1
            ath += 1
            while (i<=n) and n%i>0 :
                i+=1
        if n%i==0:
            return i
        else:
            return -1