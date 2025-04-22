class Solution:
    def canJump_gas(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
        return True

    def canJump(self, nums: List[int]) -> bool:
        reachable = [False]*len(nums)
        dist=0
        for i in range(len(nums)-1, -1, -1):
            reachable[i] = nums[i]>=dist
            if reachable[i]:
                dist=1
            else:
                dist+=1
        return reachable[0]
