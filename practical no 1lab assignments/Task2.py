print("\n===== PRACTICAL 1 : LAB ASSIGNMENT 2 =====")

v_name = input("Vendor Name: ")
year = int(input("Year of Association: "))
contact = input("Contact Number: ")
email = input("Email ID: ")

total = 0

print("\nEnter purchase amount for 12 months:")

for i in range(1, 13):
    amt = float(input(f"Month {i}: "))
    total += amt

print("\n--- Annual Purchase Report ---")
print("Vendor:", v_name)
print("Association Year:", year)
print("Contact:", contact)
print("Email:", email)
print("Total Annual Purchase:", total)
