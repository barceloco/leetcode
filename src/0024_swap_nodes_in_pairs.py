# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        anchor = ListNode(0, head)
        tail = anchor
        while tail.next and tail.next.next:
            nbr1, nbr2 = tail.next, tail.next.next
            tail.next = nbr2
            tmp = nbr2.next
            nbr1.next = nbr2.next
            tail.next.next = nbr1
            tail = tail.next.next
        return anchor.next
