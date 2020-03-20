
def root():
        A=float(input("Enter Value of root:"))
        B=float(input("Enter Number to which Root will be applied:"))
        if A==0:
            print("Math Error")
            
        elif B==0:
            print(0)
            
        else:
            C=B**(1/A)
            print(C)
            
