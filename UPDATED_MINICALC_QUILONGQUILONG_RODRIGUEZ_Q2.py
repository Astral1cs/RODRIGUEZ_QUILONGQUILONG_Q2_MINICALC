#RODRIGUEZ
#QUILONGQUILONG

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero, please try again."
    return a / b


def getValues():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2  

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choicedong = input("Choose an operation (1-4): ")

if choicedong in ["1", "2", "3", "4"]:
    
    num1, num2 = getValues()

    if choicedong == "1":
        answer = add(num1, num2)
    elif choicedong == "2":
        answer = subtract(num1, num2)
    elif choicedong == "3":
        answer = multiply(num1, num2)
    elif choicedong == "4":
        answer = divide(num1, num2)

    print("Answer:", answer)
else:
    print("Invalid choices.")