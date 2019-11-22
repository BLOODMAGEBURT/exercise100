# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     salary
   Description :
   Author :       Administrator
   date：          2019/11/1 0001
-------------------------------------------------
   Change Activity:
                   2019/11/1 0001:
-------------------------------------------------
"""
from abc import abstractmethod, ABCMeta


class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    @property
    def working_hour(self):
        return self.working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self.working_hour = working_hour

    def get_salary(self):
        return 150 * self.working_hour


if __name__ == '__main__':
    burt = Programmer('burt')
    burt.working_hour = 150
    print(burt.get_salary())
