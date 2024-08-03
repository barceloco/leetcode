class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings =  [[] for _ in range(numRows)]
        print(strings)
        if (numRows == 1) or (numRows >= len(s)):
            return s
        for i in range(len(s)):
            pos_mod = i % (numRows-1)
            pos_div = i // (numRows-1)
            if (pos_div % 2 == 0) :
                string_id = pos_mod
            else:
                string_id = numRows - pos_mod - 1
            print(string_id)
            strings[string_id].append(s[i])
        for i in range(numRows):
            strings[i] = "".join(strings[i])
        return "".join(strings) 
