#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:16:58 2017

@author: adi
"""

import banko_points    

def make_bet(choice,p1a,p1b,p2):
   
    if(choice == '1'):
        if (p1a < p2 < p1b) or (p1b < p2 < p1a):
            print("Congratulations! You Win This Round and Ten Points.")
            banko_points.points(1)
        else:    
            print("Oops! You Lose This Round and Ten Points.")
            banko_points.points(2)
            
    if(choice == '2'):
        if (p1a < p2 < p1b) or (p1b < p2 < p1a):
            print("You Could Have Won This Round. Unfortunate Choice.")
            banko_points.points(3)
        else:    
            print("You Would Have Lost This Round. Excellent Choice.")
            banko_points.points(3)
            
    if(choice == '3'):
        if (p1a == p2) and (p1b != p2):
            print("Godlike! You Win This Round and 30 Points.")
            banko_points.points(4)
        elif (p1b == p2) and (p1a != p2):
            print("Godlike! You Win This Round and 30 Points.")
            banko_points.points(4)
        elif (p1a == p1b == p2):    
            print("Jackpot! You Win This Round and 60 Points")
            banko_points.points(5)
        else:
            print("Oh My! You Lose This Round and 30 Points.")                
            banko_points.points(6)
