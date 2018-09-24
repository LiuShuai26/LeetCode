# 基础题
# 使用while循环遍历链表
# getattr(cur.next, 'val', None)获取cur.next的属性val


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        cur = head
        Gset = set(G)
        ans = 0
        while cur:
            if (cur.val in Gset and getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next
        return ans
