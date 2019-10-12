# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise15
   Description :
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def condition(marks):
    """
    条件运算符，成绩>= 90 为A, 60-89 为B, 60一下为C
    :param marks:
    :return:
    """
    if marks >= 90:
        print('A')
    elif marks >= 60:
        print('B')
    else:
        print('C')


if __name__ == '__main__':
    condition(91)
    condition(59)
    condition(78)
