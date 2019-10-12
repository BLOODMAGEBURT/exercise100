# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise20
   Description :   球从100m落下，每次弹为上次的一半，求经过10次之后，共运动了多少m，第10次弹多高
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def exercise20(high, times):
    """
    球的运动距离，和第几次的高度
    :param high: 高度
    :param times: 次数
    :return:
    """
    my_list = [high, ]
    for i in range(1, times + 1):
        high = float(high) / 2
        if i == times:
            my_list.append(high)
            print(my_list)
            print('第%d次的时候跳%.5f高' % (i, high))
        else:
            my_list.append(high * 2)
    print('总共的运动距离是%.5f' % (sum(my_list),))


if __name__ == '__main__':
    exercise20(100, 10)
