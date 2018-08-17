# -*- coding: UTF-8 -*-
"""用两个栈实现队列"""
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""

class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
        pass
    def pop(self):
        if len(self.stack1)>0:
            self.stack2=self.stack1[::-1]
            temp = self.stack2.pop()
            self.stack1=self.stack2[::-1]
            return temp
        else:
            return None
"""Better Method 2"""
# class Solution:
#     def __init__(self):
#         self.stack1=[]
#         self.stack2=[]
#     def push(self, node):
#         # write code here
#         self.stack1.append(node)
#         pass
#     def pop(self):
#         if self.stack2 == []:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#             return self.stack2.pop()
#         else:
#             return self.stack2.pop()
sl=Solution()
sl.push(1)
sl.push(2)
print(sl.pop())
print(sl.pop())
print(sl.pop())

print([21,34,5].remove(21))
