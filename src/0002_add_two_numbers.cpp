/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carryover = 0;
        ListNode* anchor = new ListNode();
        ListNode* tail = anchor;

        // while (l1 or l2 or (carryover != 0)) {
        //     int val1 = (l1) ? l1->val : 0;
        //     int val2 = (l2) ? l2->val : 0;
        while (l1 != nullptr || l2 != nullptr || carryover > 0) {
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;
            int sum = val1 + val2 + carryover;
            int val = sum % 10;
            carryover = sum / 10;

            ListNode* nextNode = new ListNode(val);
            tail->next = nextNode;
            tail = tail->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        ListNode* result = anchor->next;
        delete anchor;
        return result;
    }
};