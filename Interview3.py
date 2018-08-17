# -*- coding: UTF-8 -*-
"""查找二维数组中的数字"""
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
整数，判断数组中是否含有该整数。
"""
target=7
array=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
def Find( target, array):
        # write code here
        len_raw=len(array)
        len_col=len(array[0])
        i=len_raw-1
        j=0

        while i>=0 and j<=len_col-1:
            if target > array[i][j]:
                j=j+1
            elif target < array[i][j]:
                i=i-1
            else :
                return True
        return False
print(Find(target,array))

