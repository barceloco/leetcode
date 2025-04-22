class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i,j=0,1
        res = []
        if len(nums)==0:
            return res
        m=nums[0]
        while j<len(nums):
            n=nums[j]
            if n-m==1:
                m=n
            else:
                if j-i>1:
                    res.append("%i->%i"%(nums[i], nums[j-1]))
                else:
                    res.append("%i"%(nums[i]))
                i=j
                m=n
            j+=1
        if j-i>1:
            res.append("%i->%i"%(nums[i], nums[-1]))
        else:
            res.append("%i"%(nums[i]))
        
        return res
