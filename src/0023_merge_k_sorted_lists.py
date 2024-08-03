# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_values = []
        for k in range(len(lists)):
            while lists[k] != None:
                all_values.append(lists[k].val)
                lists[k] = lists[k].next
        all_values.sort()

        anchor = ListNode(0)
        tail = anchor
        for i in range(0,len(all_values)):
            tail.next = ListNode(all_values[i])
            tail = tail.next
        return anchor.next

####################################################################
        # correct but very slow
        if not lists or len(lists) == 0:
            return None
        while len(lists)>1:
            print(lists)
            temp = []
            for i in range(0, len(lists), 2):
                print(i)
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp
        return lists[0]

    def mergeTwoLists(self, list1: Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        if list2 == None:
            return list1 # may be None
        if list1 == None:
            return list2 # known not to be None
        # if neither list is None:
        if list1.val <= list2.val:
            print(list1.val)
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            print(list2.val)
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
