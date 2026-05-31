def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def multiply(a , b):
    return a * b
def divide(a , b):
    if b == 0:
        return "cannot divide by zero"
    return a / b
while True:
    print("\n Calculator Menu")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISON")
    print("5. EXIT")
    
    choice = input("Enter your choice (1-5) : ")
    if choice == "5":
        print("THANK YOU FOR USING CALCULATOR")
        break
    num1 = float(input("ENTER FIRST NUMBER :"))
    num2 = float(input("ENTER SECOND NUMBER :"))
    if choice == "1":
        print("RESULT = " , add(num1 , num2))
    elif choice == "2":
        print("RESULT =" , sub(num1 , num2))
    elif choice == "3":
        print("RESULT =" , multiply(num1 , num2))
    elif choice == "4":
        print("RESULT =", divide(num1 , num2))
    else:
        print("INVALID CHOICE")