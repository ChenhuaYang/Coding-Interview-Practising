# -*- coding: UTF-8 -*-
"""二进制中1的个数"""
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])

sl=Solution()
print(sl.NumberOf1(4))


