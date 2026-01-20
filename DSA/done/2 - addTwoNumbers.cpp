// https://leetcode.com/problems/add-two-numbers/

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry{0};
        ListNode* dummy = new ListNode();
        ListNode* res = dummy;
        while (l1 || l2 || carry) {
            int lvalue = l1 ? l1->val : 0;
            int rvalue = l2 ? l2->val : 0;

            int sum{ lvalue + rvalue + carry };
            carry = sum / 10;   
            sum %= 10;      

            dummy->next = new ListNode(sum);
            dummy = dummy->next;
            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }
        return res->next;
    }
};