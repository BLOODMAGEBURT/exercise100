# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise21
   Description :    猴子吃桃
   Author :       burt
   date：          2018/11/11
-------------------------------------------------
   Change Activity:
                   2018/11/11:
-------------------------------------------------
"""


def exercise21(n):
    """
    猴子吃桃，每天吃一半加1个，第10天还想吃时，剩下一个，问第一天有多少个
    可以通过递归来计算，当前天都是（后一天的数量+1）* 2 , 第10为1个
    第n天的桃子数量
    :return:
    """
    if n == 10:
        return 1
    return (exercise21(n + 1) + 1) * 2


def new(days):
    """
    通过for循环计算
    :return:
    """
    n = 1
    for day in range(10-days, 0, -1):
        n = (n + 1) * 2
    print n


if __name__ == '__main__':
    # 第一天的数量
    print exercise21(1)

    # 第9天第数量
    print exercise21(9)

    new(1)