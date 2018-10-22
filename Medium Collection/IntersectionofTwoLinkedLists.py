# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = []
        B = []
        while headA:
            A.append(headA)
            headA = headA.next
        while headB:
            B.append(headB)
            headB = headB.next
        res = None
        while A and B:
            cur = A.pop()
            if cur is not B.pop():
                break
            else:
                res = cur
        return res
