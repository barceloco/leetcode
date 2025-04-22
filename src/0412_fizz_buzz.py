class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            ans = ""
            if i%3==0:
                ans += "Fizz"
            if i%5==0:
                ans += "Buzz"
            if ans=="":
                ans="%i"%i
            res.append(ans)
        return res