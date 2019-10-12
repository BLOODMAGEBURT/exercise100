# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise7
   Description :
   Author :       burt
   date：          2018/11/6
-------------------------------------------------
   Change Activity:
                   2018/11/6:
-------------------------------------------------
"""


def list_copy():
    """
    复制alist 到 blist 中
    :return:
    """


if __name__ == '__main__':
    list_a = [1, 2, 3, 4]

    list_b = list_a[:]

    list_a.append(5)
    print('list_a是：{}-------list_b是：{}'.format(list_a, list_b))
