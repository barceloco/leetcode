class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen:
                return True
            seen[n] = True
        return False

        # works but not very fast
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False

        # correct but way too slow (rejected submission)
        seen = []
        for n in nums:
            if n in seen:
                return True
            seen.append(n)
        return False