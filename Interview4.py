
# -*- coding: UTF-8 -*-
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
"""method 1 NOT good"""
def replaceSpace(s):
    replaceS=''
    for chars in s:
        print(chars)
        if chars == ' ':
            replaceS=replaceS+'%20'
        else:
            replaceS=replaceS+chars
    return replaceS

s='we are happy'
print(replaceSpace(s))

"""method 2"""
# s.replace(' ', '20%')
"""method 3"""
import re
# ret = re.compile(' ')
# ret.sub('20%', s)
