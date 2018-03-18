# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = None
        while second.next:
            tmp = second
            second = second.next
            tmp.next = first
            first = tmp
        second.next = first
        return second

