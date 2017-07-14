#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:14:31 2017

@author: adi
"""

flag = 0

def points(result):
    
    global flag
    global num
    
    while flag == 0:
        flag = 1
        num = 0

    if result == 1:
        num = num + 10
    
    elif result == 2:
        num = num - 10
    
    elif result == 3:
        num = num
    
    elif result ==4:
        num = num + 30
    
    elif result == 5:
        num = num + 60
    
    elif result == 6:
        num = num - 30
    
    print("Your Points Are: " + str(num))    