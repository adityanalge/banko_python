#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:12:31 2017

@author: adi
"""

import banko_random_number
import banko_print_card
import banko_make_bet

class banko():
    
    def main(self):
       
        k = True
        while k:
            print('\n########################################################################################')

            x = banko_random_number.random_number()
            print("First Card Is: " + banko_print_card.print_card(x))
            p1a = x % 14
            
            x = banko_random_number.random_number()
            print("\nSecond Card Is: " + banko_print_card.print_card(x))
            p1b = x % 14
            
            while True:
                print("\nWould you like to: \n 1.Play \n 2.Pass \n 3.Moonshot \n\nEnter Choice 1,2 or 3.")
                choice =raw_input("I will: ")
                x = banko_random_number.random_number()
                if (choice == '1') or (choice == "2") or (choice == "3"):
                    break;
                    
            print("\nYour Card Is: " + banko_print_card.print_card(x))
            p2 = x % 14
            
            banko_make_bet.make_bet(choice,p1a,p1b,p2)   
            
            while True:
                f = raw_input("\nPress Y/y to Keep Playing and Q/q to Quit: ")
                if f == 'y' or f == 'Y':
                    k = True
                    break;
                elif f == 'q' or f == 'Q':
                    k = False
                    break;
                else:
                    print("Invalid Choice! Choose Again")
                    
if __name__ == '__main__':
    banko().main()            