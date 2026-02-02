n = int(input())

for i in range(1, n + 1):
    # print leading spaces
    for s in range(n - i):
        print("  ", end="")

    # print stars with gap
    for j in range(i):
        print("*   ", end="")

    print()
