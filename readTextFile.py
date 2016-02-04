#!/usr/bin/env python
# -*- coding:utf-8 -*-  
'''
read and display text file
Created on 2016年2月4日

@author: zunyuan.jy
'''

# get file name
fname = raw_input('Enter filename:')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
    

