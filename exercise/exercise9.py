# -*- coding: utf-8 -*-
import time , threading
"""
-------------------------------------------------
   File Name：     exercise9
   Description :
   Author :       burt
   date：          2018/11/7
-------------------------------------------------
   Change Activity:
                   2018/11/7:
-------------------------------------------------
"""


def sleep_a_second():
    """
    暂停一秒，再执行操作
    :return:
    """
    print 'before: %s' % (format_time(),)
    time.sleep(1)
    print 'after: %s' % (format_time(),)
    print 'now execute the python code'


def format_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


if __name__ == '__main__':
    sleep_a_second()
