// https://leetcode.com/problems/reverse-linked-list/

// Definition for singly-linked list.
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    let rev: ListNode | null = null;
    while (head) {
        let tmp = head.next;
        head.next = rev;
        rev = head;
        head = tmp;
    }
    return rev;
};