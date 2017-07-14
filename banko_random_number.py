#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 02:36:28 2017

@author: adi
"""
from random import randint
     
def random_number():
    while True:
        y = randint(1,55)
        
        if (y != 14) and (y != 28) and (y != 42):
            break
        
    return y
