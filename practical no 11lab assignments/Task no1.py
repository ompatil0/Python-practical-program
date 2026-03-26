import matplotlib.pyplot as plt

months = [1,2,3,4,5,6,7,8,9,10,11,12]

# sample data
facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash  = [1500,1200,1340,1130,1740,1550,1650,1890,1720,1500,1300,1600]
toothpaste = [5200,5100,4550,5870,6000,7000,6800,7200,7100,6500,6200,6900]

profit = [12000,15000,13000,17000,16000,18000,20000,22000,21000,19000,17000,20000]

# a) Line plot (profit)
plt.plot(months, profit)
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline plot
plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.legend()
plt.show()

# c) Bar chart (facecream & facewash)
plt.bar(months, facecream, label="Face Cream")
plt.bar(months, facewash, label="Face Wash")
plt.legend()
plt.show()

# d) Pie chart (total sales)
total = [sum(facecream), sum(facewash), sum(toothpaste)]
labels = ["Face Cream", "Face Wash", "Toothpaste"]

plt.pie(total, labels=labels, autopct='%1.1f%%')
plt.show()