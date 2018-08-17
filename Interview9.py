# -*- coding: UTF-8 -*-
"""斐波那契数列"""
"""
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
"""Method 1"""
# class Solution:
#     def Fibonacci(self, n):
#         if n>39 :
#             return None
#         elif n<=2:
#             return 1
#         else:
#             return self.Fibonacci(n-1)+self.Fibonacci(n-2)


"""Method 1 is too Slow"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n>39 :
            return None
        elif n<=2 and n>0:
            return 1
        elif n==0:
            return 0
        elif n<0:
            return None
        else:
            f0=1
            f1=1
            for i in range(2,n):
                s=f0+f1
                f0=f1
                f1=s
            return s

sl=Solution()

print sl.Fibonacci(0)
