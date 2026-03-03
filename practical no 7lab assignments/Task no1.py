def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

while True:
    print("1.Add \n2.Sub \n3.Mul \n4.Div \n5.Mod \n6.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 6:
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print("You entered:", a, "and", b)
    
    if ch == 1:
        print("Result:", add(a, b))
    elif ch == 2:
        print("Result:", sub(a, b))
    elif ch == 3:
        print("Result:", mul(a, b))
    elif ch == 4:
        print("Result:", div(a, b))
    elif ch == 5:
        print("Result:", mod(a, b))