# -*- coding:utf-8 -*-
"""链表中倒数第k个结点"""
"""
输入一个链表，输出该链表中倒数第k个结点
# """
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""Method 1"""
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        saveValue=dict()
        key=0
        if head == None:
            return None
        while head.next != None:
            saveValue[key]=head
            key=key+1
            head = head.next
        saveValue[key]=head
        print(key)
        print(saveValue)
        if key-k+1<0 or k <=0:
            return None

        else:
            return saveValue[key-k+1]

sl=Solution()
head=ListNode(1)
p=ListNode(2)
head.next=p
print(sl.FindKthToTail(head,1))

"""Method 2"""
#代码思路：两个指针，都先指向头结点，然后让第一个指针走k-1步；到达第k个节点，
#然后两个指针同时往后移，当第一个节点到达末尾的时候，第二个节点所在位置就是倒数第k个节点了

# class Solution:
#     def FindKthToTail(self, head, k):
#         front = head
#         later = head
#         for i in range(k):
#             if front==None:
#                 return
#             if front.next == None and i==k-1:
#                 return head
#             front = front.next
#         while front.next !=None:
#             front = front.next
#             later = later.next
#         return later.next
