# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     exercise17
   Description :
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def count_num(a_str):
    """
    统计一个字符串中，有多少个字母，多少个数字，多少个其他字符
    :param a_str:
    :return:
    """
    int_num = 0
    letter_num = 0
    other_num = 0
    for i in a_str:
        if i in '1234567890':
            int_num += 1
        elif i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letter_num += 1
        else:
            other_num += 1

    print '数字有%d个，字母有%d个，其他字符有%d个' % (int_num, letter_num, other_num)


def new(a_str):
    """
    :param a_str:
    :return:
    """
    int_num = 0
    letter_num = 0
    other_num = 0
    space_num = 0
    for i in a_str:
        if i.isdigit():
            int_num += 1
        elif i.isalpha():
            letter_num += 1
        elif i.isspace():
            space_num += 1
        else:
            other_num += 1

    print '数字有%d个，字母有%d个，空格有%d个，其他字符有%d个' % (int_num, letter_num, space_num, other_num)


if __name__ == '__main__':
    count_num('areyouserious88.6 $#')
    new('areYouSerious88.6 $#')
