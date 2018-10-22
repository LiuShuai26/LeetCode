# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = nodeOdd = ListNode(0)
        nodeEvenHead = nodeEven = ListNode(0)
        while head:
            nodeOdd.next = head
            nodeOdd = nodeOdd.next
            nodeEven.next = head.next
            nodeEven = nodeEven.next
            if nodeEven:
                head = head.next.next
            else:
                head = None
        nodeOdd.next = nodeEvenHead.next
        return res.next