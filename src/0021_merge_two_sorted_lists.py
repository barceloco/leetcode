# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None
        elif list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next,list2)
                return(list1)
        else:
            list2.next= self.mergeTwoLists(list1,list2.next)
            return(list2)

        # slower without recursion:
        anchor = ListNode(0, None)
        current = anchor
        while list1  and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return anchor.next