def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select options")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
choice =input("enter a choice (1/2/3/4):")
num1=float(input("enter a num1:"))
num2=float(input("enter a num2:"))
if choice=='1':
    print( num1 ,"+" ,num2,"=" ,add(num1,num2))
elif choice== '2':
     print( num1 ,"-" ,num2,"=", sub(num1,num2) )
elif choice== '3':
     print( num1 ,"*" ,num2,"=", mul(num1,num2) )
elif choice== '4':
     print( num1 ,"/" ,num2,"=", div(num1,num2) )
else:
    print("INVALID CHOICE")
    
