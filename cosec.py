import math

def cosec():
      x=int(input("Angle in Radian or Degree?Press 1 for radian,press 2 for degree"))
      if x==1:
            a=float(input("Enter Angle in Radian"))
            b=1/math.sin(a)
            print(b)
      elif x==2:
            a = float(input("Enter Angle in Degree"))
            c=a*(0.0174)
            
            b = 1/math.sin(c)
            print(b)
        
      else:
          print("Press 1 or 2")
