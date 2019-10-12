# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise12
   Description :
   Author :       burt
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""
import math


def count_su(x, y):
    """
    计算x,y之间有多少个素数
    素数定义：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
    :param x:
    :param y:
    :return:
    """
    prime_num = []
    for i in range(x, y):
        count = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            prime_num.append(i)
    return prime_num, len(prime_num)


if __name__ == '__main__':
    result = count_su(100, 200)

    print(result[0], '共有%d个' % (result[1],))
