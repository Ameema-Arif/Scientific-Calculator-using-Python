
def factorial():
    
        X=int(input("No.:"))
        if X==0:
            print(1)
            
        else:
            for Y in range(1,X):
                Z=X*Y
                X=Z
            print("The factorial of given number is:",Z)
            
