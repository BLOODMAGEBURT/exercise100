# -*- coding: utf-8 -*-
import time
"""
-------------------------------------------------
   File Name：     exercise16
   Description :
   Author :       burt
   date：          2018/11/10
-------------------------------------------------
   Change Activity:
                   2018/11/10:
-------------------------------------------------
"""


def format_time():
    """
    输出指定格式的日期
    :return:
    """
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print time_str


if __name__ == '__main__':
    format_time()
