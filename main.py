from __future__ import print_function
from functools import partial
import os
import sys
import Sum
import Sub
import Mul
import divide
import sin
import cos
import tan
import asin
import acos
import atan
import square
import root
import sqrt
import power
import factorial
import exponential
import log
import ln
import quadratic
import percentage
import sec
import cosec
import cot
import com
import per
import inverse

stderr = partial(print, file=sys.stderr)
BANNER = """
                           _     A Scientific
                          /  _.| _   | _._|_ _ ._
                          \_(_||(_|_||(_| |_(_)|
 
                              by Umer Saeed,
                            Ameema and Sumbul.
"""

stderr(BANNER)

def close():
    print("Thanks For Using Our Calculator")

def combine():
    z=input("enter expression like this: 2+4-6*3 . BODMAS RULE WILL BE APPLIED")
    y=eval(z)
    print(y)

def menu():
    print("1-Addition \t\t 2-Subtration \t\t 3-Multiply \t\t 4-Division")
    print("5-Sin() \t\t 6-Cos() \t\t 7-Tan() \t\t 8-Sec()")
    print("9-Cosec() \t\t 10-Cot() \t\t 11-Square \t\t 12-Square Root \t\t")
    print("13-Power \t\t 14-Root \t\t 15-Expontial(e^x)")
    print("16-Factorial \t\t 17-log()\t\t 18-ln() \t\t 19-Quadratic Eq Solver")
    print("20-Inverse(x^-1) \t 21-Sin inverse \t 22-Cos Inverse \t 23.Tan Inverse" )
    print("24-Permutation \t\t 25-Combination \t 26-Percentage")
    print("27-Multiple Basic Operators At a time \t\t 28-Close")

    while True:
        try:
            choice = int(input("Enter your choice(press number):"))
            break
        except ValueError:
            print("Input must be a number!")
    if choice == 1 :
        while True:
            Sum.Sum()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 2:
        while True:
            Sub.sub()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 3:
        while True:
            Mul.multiply()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 4:
        while True:
            divide.divide()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 5:
        while True:
            sin.sin()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 6 :
        while True:
            cos.cos()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 7:
        while True:
            tan.tan()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 8:
        while True:
            sec.sec()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 9:
        while True:
            cosec.cosec()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 10:
        while True:
            cot.cot()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 11:
        while True:
            square.square()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 12:
        while True:
            sqrt.sqrt()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 13:
        while True:
            power.power()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 14 :
        while True:
            root.root()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 15:
        while True:
            exponential.exponential()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 16:
        while True:
            factorial.factorial()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 17:
        while True:
            log.log()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 18:
        while True:
            ln.ln()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 19:
        while True:
            quadratic.quadratic()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 20:
        while True:
            inverse.inv()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 21:
        while True:
            asin.asin()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 22:
        while True:
            acos.acos()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 23:
        while True:
            atan.atan()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 24:
        while True:
            per.per()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 25:
        while True:
            com.com()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 26:
        while True:
            percentage.percentage()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break
    elif choice == 27:
        while True:
            combine()
            x=int(input("press 1 to try again,press 2 to return to menu"))
            if x==1:
                continue
            if x==2:
                menu()
                break        
    elif choice == 28:
        close()
    else:
        print("Invalid Input.Try Again")
        menu()

menu()


    
