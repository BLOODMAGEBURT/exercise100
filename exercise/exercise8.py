# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise8
   Description :
   Author :       burt
   date：          2018/11/6
-------------------------------------------------
   Change Activity:
                   2018/11/6:
-------------------------------------------------
"""


def print99():
    """
    打印99乘法表
    :return:
    """
    for j in range(1, 10):
        for i in range(1, j+1):
            if i == j:
                print i, '*', j, '=', i*j
            else:
                print i, '*', j, '=', i*j,


if __name__ == '__main__':
    print99()
