# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise13
   Description :
   Author :       burt
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""
import math


def flower_num():
    """
    水仙花数
    定义：三位数，其各位数字立方和等于该数本身，例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
    :return:
    """
    num = []
    for i in xrange(100, 1000):

        if i == math.pow(i/100, 3) + math.pow(i/10 % 10, 3) + math.pow(i % 10, 3):
            num.append(i)
    return num

    """
    还可以使用幂运算符
    
    i ** 3
    """


if __name__ == '__main__':
    print flower_num()
