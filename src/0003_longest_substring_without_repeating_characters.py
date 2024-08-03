class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxlen = max(right - left + 1, maxlen)

        return maxlen
