import numpy as np

# Create 4x4 identity matrix
identity = np.eye(4)

print("4x4 Identity Matrix:")
print(identity)

print("LAB ASSIGNMENT 1 (b): 3x3 Matrices\n")

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition (A + B):")
print(A + B)

print("\nMultiplication (A x B):")
print(np.dot(A, B))