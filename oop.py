#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value,int):
            raise ValueError('must be int')
        if value < 0 or value > 100:
            raise ValueError('must more than 0  or  less than 100')
        self._score = value

    @classmethod
    def get_hobby(cls):
        return cls._score


s = Student()

s.score = 60

print s.score


weekly = Enum('Weekly', ('Mon', 'Tus', 'Wen', 'Th', 'Fri'))

print weekly.Tus
