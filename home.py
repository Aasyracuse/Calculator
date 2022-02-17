def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("(1.Add/2.Subtract/3.Multiply/4.Divide)")

choice= input("Choose a operation (1,2,3,4)")
while True:  
    if choice in ('1','2','3','4'):
        num1= input("Enter your first number: ")
        num2= input("Enter your second number: ")
    if choice == '1':
        add(num1 + num2)

    
else:
    print("Invalid Input")
