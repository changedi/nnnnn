#!/usr/bin/env python
# -*- coding:utf-8 -*-  

'''
Created on 2016年2月4日

@author: zunyuan.jy
'''

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!'

displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2 + 9j)
displayNumType('xxx')

