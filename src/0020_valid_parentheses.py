class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in closeToOpen:
                stck.append(c)
                continue
            if not stck or stck[-1]!=closeToOpen[c]:
                return False
            stck.pop()
        return not stck

        #slightly slower
        stck = []
        cl = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for c in s:
            if c in cl.keys():
                stck.append(cl[c])
                continue
            if len(stck)==0:
                return False
            if not c == stck.pop():
                return False
        if len(stck)>0:
            return False
        return True