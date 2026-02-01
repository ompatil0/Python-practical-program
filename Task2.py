# -------------------------------
# PATTERN 1 : Alphabet Increasing
# -------------------------------
print("PATTERN 1:\n")

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\n-----------------------------\n")

# -------------------------------
# PATTERN 2 : ' and # Alternating
# -------------------------------
print("PATTERN 2:\n")

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print("'", end=" ")
        else:
            print("#", end=" ")
    print()

print("\n-----------------------------\n")

# -------------------------------
# PATTERN 3 : PYTHON Repetition
# -------------------------------
print("PATTERN 3:\n")

word = "python"
for i in range(len(word)):
    print(word[i] * (i + 1))

print("\n-----------------------------\n")

# -------------------------------
# PATTERN 4 : PYTHON Building
# -------------------------------
print("PATTERN 4:\n")

word = "python"
for i in range(1, len(word) + 1):
    print(word[:i])
