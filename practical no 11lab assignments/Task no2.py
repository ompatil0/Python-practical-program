import matplotlib.pyplot as plt

companies = ["Microsoft","Google","Amazon","IBM","Amdocs"]
recruit = [120,150,180,90,110]

# a) Bar chart
plt.bar(companies, recruit)
plt.title("Recruitment")
plt.show()

# b) Pie chart
plt.pie(recruit, labels=companies, autopct='%1.1f%%')
plt.show()

# c) Customized Pie chart
plt.pie(recruit, labels=companies, autopct='%1.1f%%',
        explode=[0,0.1,0,0,0])
plt.show()

# d) Doughnut chart
plt.pie(recruit, labels=companies)
centre = plt.Circle((0,0),0.5,color='white')
plt.gca().add_artist(centre)
plt.show()

# e) Compare IBM & Amdocs
plt.bar(["IBM","Amdocs"], [90,110])
plt.title("IBM vs Amdocs")
plt.show()