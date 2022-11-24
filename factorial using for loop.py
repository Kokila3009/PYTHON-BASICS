#to demonstrate factorial

x=int(input("Enter the number  to factorial calculation"))

fact=1

if(x==0):
    
    print("the factorial of",x,"is 1")

        
        
elif(x<0):
    
    print("Factorial doesn't exist")

else:
    
     for i in range(1,(x+1)):
        
        fact=fact*i
     print("factorial of ",x,"is",fact,)
        
