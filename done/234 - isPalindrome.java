/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode s = head, f = head;
        while (f != null && f.next != null) {
            f = f.next.next;
            s = s.next;
        }

        ListNode r = null;
        while (s != null) {
            ListNode tmp = s.next;
            s.next = r;
            r = s;
            s = tmp;
        }

        ListNode l = head;
        while (r != null) {
            if (l.val != r.val) {
                return false;
            }
            l = l.next;
            r = r.next;
        }

        return true;
    }
}