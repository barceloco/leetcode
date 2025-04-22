class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_counts(strx):
            counts = {}
            for c in strx:
                if c in counts.keys():
                    counts[c]+=1
                else:
                    counts[c]=1
            return counts
        counts_s = get_counts(s)
        counts_t = get_counts(t)
        return counts_s==counts_t
