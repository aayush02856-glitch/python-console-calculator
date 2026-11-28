# Function defination

def Input1():
    i = int(input("1st Number : "))
    return i
def Input2():
    i = int(input("2nd Number : "))
    return i

def addition(x,y):
    return x+y
def subtraction(x,y): 
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y == 0 :
        print("Error ! Zero can't divide anything in this code ")
    else :
        return x/y

# Actual code 

print("It is a Simple Console Level Calculator.")
l = 0
while l>=0 :
    print("\nSelect the operation.")
    print("1 = Addition","2 = Subtraction","3 = Multiplication","4 = Division",sep="\n")
    try:
        n = int(input("\nEnter the Numerical Value of the operations : "))
    except ValueError:
        print("Invalid input !\n")
    else:
# condition for Addition
        if(n==1):
            print("Addition of two numbers.")
            print("The Sum of the numbers is",addition(Input1(),Input2()))               # Function call
# condition for Subtraction
        elif(n==2):
            print("Subtraction of two numbers.")
            print("The difference of the numbers is",subtraction(Input1(),Input2()))     # Function call
# condition for Multiplication
        elif(n==3):
            print("Multiplication of two numbers.")
            print("The product of the numbers is",multiplication(Input1(),Input2()))     # Function call
# condition for Division
        elif(n==4):
            print("Division of two numbers.")
            print("The Quotient of the numbers is",division(Input1(),Input2()))          # Function call
    l = l+1
 