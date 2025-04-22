class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n^ res
        return res

        # ns = set()
        # for n in nums:
        #     if n in ns:
        #         ns.remove(n)
        #     else:
        #         ns.add(n)
        # return next(iter(ns))