print("LAB ASSIGNMENT 2: 5x3 x 3x2 Matrix Multiplication\n")

print("Enter elements for 5x3 Matrix:")

A = []
for i in range(5):
    row = []
    for j in range(3):
        val = int(input(f"A[{i}][{j}] : "))
        row.append(val)
    A.append(row)

A = np.array(A)

print("\nEnter elements for 3x2 Matrix:")

B = []
for i in range(3):
    row = []
    for j in range(2):
        val = int(input(f"B[{i}][{j}] : "))
        row.append(val)
    B.append(row)

B = np.array(B)

C = np.dot(A, B)

print("\nMatrix A (5x3):")
print(A)

print("\nMatrix B (3x2):")
print(B)

print("\nProduct Matrix (5x2):")
print(C)