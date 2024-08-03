class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # assume A=nums1 is shorter than B=nums2
        lenA = len(nums1)
        lenB = len(nums2)
        if lenA > lenB:
            return self.findMedianSortedArrays(nums2, nums1)
        
        lenAB = lenA + lenB
        half = lenAB // 2

        l,r = 0, lenA-1
        while True:
            m = (l+r) // 2
            n = half - m - 2

            Al = nums1[m] if m >= 0 else float("-infinity")
            Ar = nums1[m+1] if m+1 < lenA else float("infinity")
            Bl = nums2[n] if n >= 0 else float("-infinity")
            Br = nums2[n+1] if n+1 < lenB else float("infinity")

            if Al <= Br and Bl <= Ar: # found partition
                if lenAB % 2: 
                    return min(Ar, Br)
                return 0.5*(max(Al, Bl) + min(Ar, Br))

            if Al > Br:
                r = m-1
            else:
                l = m+1
            
