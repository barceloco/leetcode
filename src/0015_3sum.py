class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j<k:
                total = a + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    candidate = [a, nums[j], nums[k]]
                    triplets.append(candidate)
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return triplets

        # still too slow?!
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    candidate = [nums[i], nums[j], nums[k]]
                    if candidate not in triplets:
                        triplets.append(candidate)
        return triplets


        # still too slow
        nums.sort()
        if len(nums)< 3:
            return []
        triplets = []
        for a in range(len(nums)-2):
            for b in range(a+1, len(nums)-1):
                for c in range(b+1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        candidate = [nums[a], nums[b], nums[c]]
                        if candidate not in triplets:
                            triplets.append(candidate)
        return triplets

        # too slow:
        print(len(nums))
        if len(nums)< 3:
            return []
        triplets = []
        for a in range(len(nums)-2):
            for b in range(a+1, len(nums)-1):
                for c in range(b+1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        candidate = sorted([nums[a], nums[b], nums[c]]) 
                        if candidate not in triplets:
                            triplets.append(candidate)
        return triplets

            