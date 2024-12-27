/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode *s = head, *f = head;
        while (f and f->next) {
            f = f->next->next;
            s = s->next;
        }

        ListNode* r = nullptr;
        while (s) {
            ListNode* tmp = s->next;
            s->next = r;
            r = s;
            s = tmp;
        }

        ListNode* l = head;
        while (r) {
            if (l->val != r->val) {
                return false;
            }
            l = l->next;
            r = r->next;
        }

        return true; 
    }
};