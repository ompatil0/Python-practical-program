balance = 0

def show():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)
    print("Updated Balance:", balance)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")

while True:
    print("\n1.Display Balance\n2.Deposit\n3.Withdraw\n4.Exit")
    ch = int(input("Enter choice: "))
    
    if ch == 4:
        break
    
    if ch == 1:
        show()
    elif ch == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif ch == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)