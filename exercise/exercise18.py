# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise18
   Description :
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def exercise18(param, times):
    """
    sum = 2 + 22 + 222 + 2222 + 22222
    :param times: 次数
    :param param: 参数
    :return:
    """
    total = 0
    for i in xrange(1, times+1):
        if i != times:
            print '%s+' % (param*i,),
        else:
            print '%s' % (param*i,),
        total += int(param*i)
    print '和为%d' % (total,)


def new(param, times):
    """
    放在一个数组里面
    :param param:
    :param times:
    :return:
    """
    my_list = []
    for i in xrange(1, times+1):
        my_list.append(str(param)*i)
    print '%d = %s' % (sum([int(x) for x in my_list]), '+'.join(my_list))


if __name__ == '__main__':
    exercise18('3', 4)
    new('2', 3)
    new(2, 3)
