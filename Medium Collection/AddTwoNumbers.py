# Definition for singly-linked list.

# 在除法中得到整数，使用截除运算//向下取整


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0; n2 = 0
        ten = 1
        while l1:
            print(l1.val)
            n1 += l1.val*ten
            l1 = l1.next
            ten *= 10
        ten = 1
        while l2:
            n2 += l2.val*ten
            l2 = l2.next
            ten *= 10
        n3 = n1 + n2
        n3 = int(n3)
        print(n1, n2)
        res = node = ListNode(0)
        while n3:
            node.next = ListNode(n3 % 10)
            n3 = n3//10
            node = node.next
        return res.next

