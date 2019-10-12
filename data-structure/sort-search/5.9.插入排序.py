# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     5.9.插入排序
   Description :
   Author :       Administrator
   date：          2019/10/12 0012
-------------------------------------------------
   Change Activity:
                   2019/10/12 0012:
-------------------------------------------------
"""


def insertion_sort(alist):
    size = len(alist)
    # 先循环获取从第二项到最后一项
    for i in range(1, size):
        current_value = alist[i]
        for j in range(i - 1, -1, -1):
            # 将值依次与前方的数字做比较， 如果比前一项小，则前一项往后移一位，直到比前一项大为止
            if alist[j] > current_value:
                alist[j + 1] = alist[j]
                # 需要注意如果比第一项大的时候
                if j == 0:
                    alist[0] = current_value
            else:
                alist[j + 1] = current_value
                break
    return alist


def insertion_sort2(alist):
    """
    使用while的方式
    :param alist:
    :return:
    """
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value

    return alist


if __name__ == '__main__':
    alist = [45, 20, 15, 30, 25, 10]
    print(insertion_sort2(alist))
