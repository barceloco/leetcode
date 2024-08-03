# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        anchor = ListNode(0, head)
        current = anchor.next
        nbr_nodes = 0
        while current != None:
            nbr_nodes += 1
            current = current.next
        newseq = anchor        
        for i in range(nbr_nodes - n):
            newseq = newseq.next
        if newseq.next != None:
            newseq.next = (newseq.next).next
        else:
            newseq.next = None
        for i in range(n-1):
            newseq = newseq.next
        return anchor.next