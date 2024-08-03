5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longlen = 0
        longpal = ""
        for i in range(len(s)):
            # odd length
            a, b = i, i
            while (a >= 0) and (b<len(s)) and (s[a]==s[b]):
                if (b-a+1 > longlen):
                    longlen = b-a+1
                    longpal = s[a:b+1]
                a -= 1
                b += 1
            # odd length
            a, b = i, i+1
            while (a >= 0) and (b<len(s)) and (s[a]==s[b]):
                if (b-a+1 > longlen):
                    longlen = b-a+1
                    longpal = s[a:b+1]
                a -= 1
                b += 1
        return longpal
