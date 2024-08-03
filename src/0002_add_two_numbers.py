# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        anchor = ListNode()
        current = anchor
        
        while l1 or l2 or carryover:
            res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryover
            carryover = res // 10
            value = res % 10
            current.next = ListNode(value)
            current = current.next 
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return anchor.next
