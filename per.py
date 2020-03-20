import math


def per():
        print("Enter values to calculate nPr:")
        n = int(input("Enter value of n:"))
        r = int(input("Enter value of r:"))
        if (n>=r):
            result = (math.factorial(n))/(math.factorial(n-r))
            print(n,"P",r,"=",result)
            
        else:
            print("Permutation is not possible")
            
