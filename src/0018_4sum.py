class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        quad = []
        def kSum(k, start, target):
            if k > 2:
                for i in range(start, len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            
            l = start
            r = len(nums)-1
            while l<r:
                d = nums[l] + nums[r] - target
                if d > 0:
                    r -= 1
                elif d < 0:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1] :
                        l+=1
        kSum(4, 0, target)
        return res


#FASTER:
class Faster_Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(nums, start, target, k):

            res = []

            if start >= len(nums):
                return res

            avg = target // k

            if avg < nums[start] or avg > nums[-1]:
                return res

            if k == 2:
                return twoSum(nums, start, target)

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                for subset in kSum(nums, i + 1, target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

            return res

        def twoSum(nums, start, target):
            
            ans = []
            i, j = start, len(nums) - 1

            while i < j:
                total = nums[i] + nums[j]

                if total < target or (i > start and nums[i] == nums[i - 1]):
                    i += 1

                elif total > target or (j < len(nums) - 1 and nums[j] == nums[j + 1]):
                    j -= 1

                else:
                    ans.append([nums[i], nums[j]])
                    i += 1
                    j -= 1

            return ans

        nums.sort()
        return kSum(nums, 0, target, 4)

                 
