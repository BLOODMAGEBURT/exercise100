# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise14
   Description :
   Author :       burt
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""


def zhi_shu(n, mnum):
    """
    将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
    :param n:
    :return:
    """
    nums = mnum
    count = 0
    for i in range(2, n):
        if n % i == 0:
            nums.append(str(i))
            # print nums
            return zhi_shu(n / i, nums)
        count += 1
        if count == n - 2:
            nums.append(str(n))
    # n 已经改变了，我还没想好 怎么处理
    return '%d=%s' % (n, '*'.join(nums))


def new_zhi_shu(n):
    """
    通过while 来处理
    :param n:
    :return:
    """
    print('%d = ' % (n,), )
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n /= i
                if n != 1:
                    print('%d*' % (i,), )
                else:
                    print(i)
                break


if __name__ == '__main__':
    print(zhi_shu(90, []))

    print(new_zhi_shu(100))


class AssignValue(object):
    def __init__(self, value, name):
        self.value = value
        self.name = name


my_value = AssignValue(6, 'burt')
my_value1 = AssignValue(7, 'girl')
print('value 为: {0.name}{1.value}'.format(my_value, my_value1))
