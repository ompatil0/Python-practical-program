print("\n===== PRACTICAL 2 : LAB ASSIGNMENT 1 =====")

V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

I = V / R

print("Current =", I, "Ampere")

if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
