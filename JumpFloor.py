# -*- coding:utf-8 -*-
"""跳台阶"""
"""一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。"""
class Solution:
    def jumpFloor(self, number):
        f0=1
        f1=1
        if number == 0:
            return 1
        if number == 1:
            return 1
        while number>=2:
            f0,f1=f1,f1+f0
            number=number-1
        return f1

sl=Solution()
print(sl.jumpFloor(4))
