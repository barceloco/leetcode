class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for pos, num in enumerate(nums):
            if num in hmap.keys():
                return [hmap[num], pos]
            else:
                hmap[target-num]=pos
