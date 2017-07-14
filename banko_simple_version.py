#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 02:36:28 2017

@author: adi
"""
# This is a simple version of the entire project combined into one script

from random import randint

face_card = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
flag = 0
  
def random_number():
    while True:
        y = randint(1,55)
        if (y != 14) and (y != 28) and (y != 42):
            break
        
    return y
    
def print_card(x):
 
    
    if (x == 1):
        str = (face_card[0] + " of Hearts")
    elif (x == 2):
        str = (face_card[1] + " of Hearts")
    elif (x == 3):
        str = (face_card[2] + " of Hearts")
    elif (x == 4):
        str = (face_card[3] + " of Hearts")
    elif (x == 5):
        str = (face_card[4] + " of Hearts")
    elif (x == 6):
        str = (face_card[5] + " of Hearts")
    elif (x == 7):
        str = (face_card[6] + " of Hearts")
    elif (x == 8):
        str = (face_card[7] + " of Hearts")
    elif (x == 9):
        str = (face_card[8] + " of Hearts")
    elif (x == 10):
        str = (face_card[9] + " of Hearts")
    elif (x == 11):
        str = (face_card[10] + " of Hearts")
    elif (x == 12):
        str = (face_card[11] + " of Hearts")
    elif (x == 13):
        str = (face_card[12] + " of Hearts")
    elif (x == 15):
        str = (face_card[0] + " of Spades")
    elif (x == 16):
        str = (face_card[1] + " of Spades")
    elif (x == 17):
        str = (face_card[2] + " of Spades")
    elif (x == 18):
        str = (face_card[3] + " of Spades")
    elif (x == 19):
        str = (face_card[4] + " of Spades")
    elif (x == 20):
        str = (face_card[5] + " of Spades")
    elif (x == 21):
        str = (face_card[6] + " of Spades")
    elif (x == 22):
        str = (face_card[7] + " of Spades")
    elif (x == 23):
        str = (face_card[8] + " of Spades")
    elif (x == 24):
        str = (face_card[9] + " of Spades")
    elif (x == 25):
        str = (face_card[10] + " of Spades")
    elif (x == 26):
        str = (face_card[11] + " of Spades")
    elif (x == 27):
        str = (face_card[12] + " of Spades")
    elif (x == 29):
        str = (face_card[0] + " of Diamonds")
    elif (x == 30):
        str = (face_card[1] + " of Diamonds")
    elif (x == 31):
        str = (face_card[2] + " of Diamonds")
    elif (x == 32):
        str = (face_card[3] + " of Diamonds")
    elif (x == 33):
        str = (face_card[4] + " of Diamonds")
    elif (x == 34):
        str = (face_card[5] + " of Diamonds")
    elif (x == 35):
        str = (face_card[6] + " of Diamonds")
    elif (x == 36):
        str = (face_card[7] + " of Diamonds")
    elif (x == 37):
        str = (face_card[8] + " of Diamonds")
    elif (x == 38):
        str = (face_card[9] + " of Diamonds")
    elif (x == 39):
        str = (face_card[10] + " of Diamonds")
    elif (x == 40):
        str = (face_card[11] + " of Diamonds")
    elif (x == 41):
        str = (face_card[12] + " of Diamonds")
    elif (x == 43):
        str = (face_card[0] + " of Clubs")
    elif (x == 44):
        str = (face_card[1] + " of Clubs")
    elif (x == 45):
        str = (face_card[2] + " of Clubs")
    elif (x == 46):
        str = (face_card[3] + " of Clubs")
    elif (x == 47):
        str = (face_card[4] + " of Clubs")
    elif (x == 48):
        str = (face_card[5] + " of Clubs")
    elif (x == 49):
        str = (face_card[6] + " of Clubs")
    elif (x == 50):
        str = (face_card[7] + " of Clubs")
    elif (x == 51):
        str = (face_card[8] + " of Clubs")
    elif (x == 52):
        str = (face_card[9] + " of Clubs")
    elif (x == 53):
        str = (face_card[10] + " of Clubs")
    elif (x == 54):
        str = (face_card[11] + " of Clubs")
    elif (x == 55):
        str = (face_card[12] + " of Clubs")
        
    return str
    
def make_bet(choice,p1a,p1b,p2):
   
    if(choice == '1'):
        if (p1a < p2 < p1b) or (p1b < p2 < p1a):
            print("Congratulations! You Win This Round and Ten Points.")
            points(1)
        else:    
            print("Oops! You Lose This Round and Ten Points.")
            points(2)
            
    if(choice == '2'):
        if (p1a < p2 < p1b) or (p1b < p2 < p1a):
            print("You Could Have Won This Round. Unfortunate Choice.")
            points(3)
        else:    
            print("You Would Have Lost This Round. Excellent Choice.")
            points(3)
            
    if(choice == '3'):
        if (p1a == p2) and (p1b != p2):
            print("Godlike! You Win This Round and 30 Points.")
            points(4)
        elif (p1b == p2) and (p1a != p2):
            print("Godlike! You Win This Round and 30 Points.")
            points(4)
        elif (p1a == p1b == p2):    
            print("Jackpot! You Win This Round and 60 Points")
            points(5)
        else:
            print("Oh My! You Lose This Round and 30 Points.")                
            points(6)


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
    
class banko():
    
    def main(self):
       
        k = True
        while k:
            print('\n########################################################################################')

            x = random_number()
            print("First Card Is: " + print_card(x))
            p1a = x % 14
            
            x = random_number()
            print("\nSecond Card Is: " + print_card(x))
            p1b = x % 14
            
            while True:
                print("\nWould you like to: \n 1.Play \n 2.Pass \n 3.Moonshot \n\nEnter Choice 1,2 or 3.")
                choice =raw_input("I will: ")
                x = random_number()
                if (choice == '1') or (choice == "2") or (choice == "3"):
                    break;
                    
            print("\nYour Card Is: " + print_card(x))
            p2 = x % 14
            
            make_bet(choice,p1a,p1b,p2)   
            
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
