n = 5

# Pattern 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

# Pattern 2
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

print()

# Pattern 3 (reverse numbers)
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print()

# Pattern 4 (binary)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j % 2, end="")
    print()

print()

# Pattern 5 (even numbers)
num = 2
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()

print()

# Star Pattern
for i in range(1, n + 1):
    print("*" * i)
