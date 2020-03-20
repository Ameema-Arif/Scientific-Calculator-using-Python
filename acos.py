import math


def acos():
    
        Z=int(input("Ans in Radian or Degree?1.radian,2.degree"))
        if Z==1:
            X=float(input("Value?"))
            Y=math.acos(X)
            print(Y)
        elif Z==2:
            X=float(input("Value?"))
            Y=math.acos(X)
            Y=Y*(180/3.14)
            print(Y)
        else:
            print("Please enter 1 or 2")
