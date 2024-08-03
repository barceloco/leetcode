class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # also consider: using sorted, which sorts the strings and reduces the required checks to comparing the first and last strings, only (because they are sorted)
        lengths = []
        for i in range(len(strs)):
            lengths.append(len(strs[i]))
        shared_length = min(lengths)
        # print(lengths, shared_length)
        shared_prefix = ""
        is_identical = True
        idx = 0
        while is_identical and idx < shared_length:
            for q in range(1, len(strs)):
                if strs[0][idx] != strs[q][idx]:
                    is_identical = False
            if is_identical:
                idx += 1
                shared_prefix = strs[0][0:idx]
        return shared_prefix

