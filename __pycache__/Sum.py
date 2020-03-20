import pr
def Sum():
     result=pr.r 
     
     while True:
          if result!=0:
               x=input("Do you want to use previous result as 1st value?Press Y/y for Yes Or N/n for No ")
               if x=='Y' or x=='y':
                    B=float(input("2nd Value:"))
                    C=result+B
                    print(C)
                    result=C
                    X=int(input("Press 1 to Try Again or Press 2 to return to Main Menu:"))
                    if X==1:
                      continue
                    elif X==2:
                      menu()
               else:
                       A=float(input("1st Value:"))
                       B=float(input("2nd Value:"))
                       C=A+B
                       print(C)
                       result=C
                       X=int(input("Press 1 to Try Again or Press 2 to return to Main Menu:"))
                       if X==1:
                           continue
                       elif X==2:
                           menu()
          else:
                    
             A=float(input("1st Value:"))
             B=float(input("2nd Value:"))
             C=A+B
             print(C)
             pr.r=C
             X=int(input("Press 1 to Try Again or Press 2 to return to Main Menu:"))
             if X==1:
                 continue
             elif X==2:
                 menu()
   
