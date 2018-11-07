# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise11
   Description :
   Author :       burt
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""


def rabbit_num(n):
    """
    兔子不死： 初始有一对兔子，每对兔子在第3个月会 生下一对兔子，然后每个月都有兔子，问每个月兔子的对数
    :return:
    还是斐波那契数列问题
    """
    if n == 1 or n == 2:
        return 1
    return rabbit_num(n-1) + rabbit_num(n-2)
