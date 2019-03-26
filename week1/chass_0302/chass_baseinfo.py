#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-02 21:52
# @Author  : yang_cube
# @Site    : 
# @File    : chass_baseinfo.py
# @Software: PyCharm
# 基础语法


"""print(1)
print(2)
print(3)"""

a = 'hsdah' \
    'hadu'
print(a)
b = '你好，我的名字是："杨"'
print(b)

c = ''''nihao,
       wohis 
       haushudasjf'''
print(c)

# 占位符
name = 'yang'
age = 22
salary = 9000.9
print('我的名字是%s,我的年龄是%d,我的薪水是%.2f' % (name, age, salary))
print('我的名字是{},我的年龄是{},我的薪水是{}'.format(name, age, salary))
print('我的名字是{1},我的年龄是{1},我的薪水是{1}'.format(name, age, salary))
