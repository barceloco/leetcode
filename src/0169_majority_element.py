class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m=defaultdict(int)
        print(m)

        for num in nums:
            m[num] += 1
        
        nmax = n//2
        for key, value in m.items():
            if value > nmax:
                return key
        return 0

    def majorityElement_sort(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

    def majorityElement_slow(self, nums: List[int]) -> int:
        d = dict()
        for i, n in enumerate(nums):
            if n in d.keys():
                d[n] += 1
                if d[n] > (len(nums)+1)//2:
                    return n
            else:
                d[n] = 1
        nmax = -1
        maxn = 0
        for n in d.keys():
            if d[n]>maxn:
                maxn = d[n]
                nmax = n
        return nmax
        