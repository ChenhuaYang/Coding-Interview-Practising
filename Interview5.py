# -*- coding: UTF-8 -*-
"""从尾到头打印单链表"""
"""输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def printListFromTailToHead(listNode):
    stack=[]
    result=[]
    while listNode:
        stack.append(listNode.val)
        listNode=listNode.next
    while stack:
        result.append(stack.pop())


a=ListNode(1)
b=ListNode(2)
a.next=b
c=None
printListFromTailToHead(c)

"""method 2"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         # write code here
#         l = list()
#         while listNode:
#             l.append(listNode.val)
#             listNode = listNode.next
#         return l[::-1]#翻转,倒序
"""method 3"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
    # # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # def printListFromTailToHead(self, listNode):
    #     # write code here
    #     l = []
    #     head = listNode
    #     while head:
    #         l.insert(0, head.val)
    #         head = head.next
    #     return l
