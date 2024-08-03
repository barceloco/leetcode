# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        anchor = ListNode(0, head)
        group_anchor = anchor

        while True:
            kth = self.getKth(group_anchor, k)
            if not kth:
                break
            group_next = kth.next

            previous, current = group_next, group_anchor.next
            while current != group_next:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp
            tmp = group_anchor.next
            group_anchor.next = kth
            group_anchor = tmp
        return anchor.next

    def getKth(self, current, k):
        while current and k>0:
            current = current.next
            k-= 1
        return current