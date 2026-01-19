// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* front = dummy;
        ListNode* back = dummy;
        for (int i = 0; i <= n; i++) {
            front = front->next;
        }
        while (front) {
            back = back->next;
            front = front->next;
        }
        back->next = back->next->next;
        return dummy->next;
    }
};