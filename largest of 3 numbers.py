# to demonstrate largest of 3 numbers
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>b and a>c:
    print(a,"is larger")
elif b>c:
    print(b,"is larger")
else:
    
    print("the largest is",c)    
