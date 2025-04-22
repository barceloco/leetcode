class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[len(citations)-1-i] < i+1:
                return i
        return len(citations)

        