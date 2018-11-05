# -*- coding: utf-8 -*-


def sort_method(alist):
    """
    给一个list排序，从小到大
    :param alist:
    :return:
    """
    assert isinstance(alist, list)
    new_list = sorted(alist)
    return new_list


if __name__ == '__main__':
    print sort_method([2, 7, 5, 10, 4])

    """
    按学生年龄大小排队，从小到大
    """
    students = [('burt', 20), ('tom', 23), ('jean', 21), ('jack', 19)]
    sorted_students = sorted(students, key=lambda x: x[1])
    print 'sorted_students:', sorted_students

