class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        tmp = ""
        for c in s:
            if c not in s:
                tmp += c
            else:
                count += 1
                tmp = c
        return count + 1

        #slower:
        substrings = []
        current = []
        for i in range(len(s)):
            if s[i] not in current:
                current.append(s[i])
            else:
                substrings.append(current)
                current = [s[i]]
        substrings.append(current)
        return(len(substrings))