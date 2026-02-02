print("\n===== PRACTICAL 1 : LAB ASSIGNMENT 1 =====")

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

gross = basic + da + hra + ta
net = gross - lic

print("\n--- Salary Slip ---")
print("Name:", name)
print("ID:", emp_id)
print("Department:", dept)
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Net Salary:", net)