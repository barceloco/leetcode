class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wid = 0
        for rid in range(len(nums)):
            # print(rid, nums)
            if nums[rid] != val:
                nums[wid] = nums[rid]
                wid+=1
        # print(nums)
        return wid