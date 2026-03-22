import pandas as pd
import os

# Show current working directory (for debugging)
print("Current Path:", os.getcwd())

# Correct file path (auto detect same folder)
file_path = os.path.join(os.path.dirname(__file__), "books.csv")

# Read CSV
df = pd.read_csv(file_path)

# Show full data
print("\n--- Full Data ---")
print(df)

# b) Books of given author
a = input("\nEnter author: ")
print(df[df["author"] == a])

# c) Books of given publisher
p = input("\nEnter publisher: ")
print(df[df["publisher"] == p])

# d) Cheapest & costliest
print("\nCheapest Book:")
print(df[df["price"] == df["price"].min()])

print("\nCostliest Book:")
print(df[df["price"] == df["price"].max()])

# e) Sort by price
print("\nSorted by Price:")
print(df.sort_values("price"))