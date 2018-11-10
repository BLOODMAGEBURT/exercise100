# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise19
   Description : 获取1000以内的所有完数，like 6 = 1 +2 +3, 6即为完数
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def exercise19():
    """
    获取所有完数
    :return:
    """
    wan_shu = []
    # 循环判断，是不是所有质因数之和，参见exercise14
    for i in xrange(1, 101):
        if i == get_zhi_list(i):
            wan_shu.append(i)
    print '完数list为：',wan_shu


def get_zhi_list(n):
    """
    获取一个数字的质因数之和
    :param n:
    :return:
    """
    my_list = []
    while n != 1:
        for i in xrange(2, n+1):
            if n % i == 0:
                my_list.append(i)
                n /= i
                break
    my_list.insert(0, 1)
    print my_list
    return sum(my_list)


if __name__ == '__main__':
    exercise19()
