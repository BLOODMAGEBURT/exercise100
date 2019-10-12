# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise6
   Description :
   Author :       burt
   date：          2018/11/5
-------------------------------------------------
   Change Activity:
                   2018/11/5:
-------------------------------------------------
"""
__author__ = 'burt'


def fib(n):
    """
    斐波那契数列 
    定义：0，1，1，2，3，5，8 ……
    f0 = 0 ,
    f1 =1  ,
    fn = f(n-1) + f(n-2)    n >=2
    :param n:
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    """
    can be easier
    
    
    if n ==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    """


if __name__ == '__main__':
    print(fib(4))
