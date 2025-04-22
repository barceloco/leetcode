class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_k = len(nums)
        is_duplicate=False
        j=1
        for i in range(1,len(nums)):
            if is_duplicate:
                if nums[j-1] != nums[i]:
                    is_duplicate = False
                    nums[j] = nums[i]
                    j+=1
            else:
                if nums[j-1] == nums[i]:
                    is_duplicate = True
                nums[j] = nums[i]
                j+=1
        return j
