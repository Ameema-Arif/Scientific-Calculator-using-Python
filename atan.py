import math

def atan():
        Z=int(input("Ans in Radian or Degree?1.radian,2.degree"))
        if Z==1:
            X=float(input("Value?"))
            Y=math.atan(X)
            print(Y)
        elif Z==2:
            X=float(input("Value?"))
            Y=math.atan(X)
            Y=Y*(180/3.14)
            print(Y)
        else:
            print('Press 1 or 2')
