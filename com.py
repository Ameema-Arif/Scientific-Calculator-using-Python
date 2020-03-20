import math

def com():
    
        print("Enter values to calculate nCr:")
        n = int(input("Enter value of n:"))
        r = int(input("Enter value of r:"))
        if (n>=r):
            result = (math.factorial(n))/(math.factorial(n-r)*math.factorial(r))
            print(n,"C",r,"=",result)
            
        else:
            print("Combination is not possible")
            
        
