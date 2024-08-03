class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = None
        nums.sort()
        print(nums)
        min_dist = 1e8
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                dist = nums[i] + nums[j] + nums[k] - target
                adist = abs(dist)
                if adist < min_dist:
                    min_dist = adist
                    res = nums[i] + nums[j] + nums[k]
                if dist > 0:
                    k -= 1
                if dist < 0:
                    j += 1
                if dist == 0:
                    return res
        return res
                
