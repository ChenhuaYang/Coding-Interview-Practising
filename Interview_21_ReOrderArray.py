# -*- coding:utf-8 -*-
"""调整数组顺序使奇数位于偶数前面"""
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后
半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
"""Method 1 ocupy too much space"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        len_array=len(array)
        tmp1=[]
        tmp2=[]
        for i in range(len_array):
            if array[i]%2!=0:
                tmp1.append(array[i])
            else:
                tmp2.append(array[i])
        array=tmp1+tmp2
        return array

