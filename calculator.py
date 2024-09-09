#define your operations
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

#create a user interface
print("Select Operation")

print("1. Add")
print("2. Divide")
print("3. Subtract")
print("4. Multiply")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

#execute operation and display result
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif choice == '2':
    print(f"{num1} / {num2} = {divide(num1, num2)}")

elif choice == '3':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif choice == '4':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

else:
    print("Invalid Input, Try Again")