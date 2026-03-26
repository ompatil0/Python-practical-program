import pandas as pd

df = pd.read_excel("employee.xlsx")

# a) Employees in Automobile
print("\nAutomobile Employees:")
print(df[df["Department"] == "Automobile"])

# b) Employee by ID
eid = int(input("\nEnter Employee ID: "))
print(df[df["EmpID"] == eid])

# c) Developers list
print("\nDevelopers:")
print(df[df["Designation"] == "Developer"])