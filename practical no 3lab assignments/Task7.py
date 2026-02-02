# Input using while loop with validation
while True:
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > 0 and end > 0 and start < end:
        break
    else:
        print("Invalid input! Start must be smaller than end and both > 0.")

print("\nPrime numbers between", start, "and", end, "are:")

# Checking primes using for loop
for num in range(start, end + 1):

    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")
