# -*- coding:utf-8 -*-
"""反转链表"""
"""
输入一个链表，反转链表后，输出新链表的表头。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        p=pHead
        l=[]
        while p!=None :
            l.append(p)
            p=p.next
        len_l=len(l)
        for i in range (len_l-1,0,-1):
            l[i].next=l[i-1]
        l[i-1].next=None
        return l[-1]

sl=Solution()
head=ListNode(1)
p=ListNode(2)
head.next=p
print (head.next)
print (sl.ReverseList(head))
