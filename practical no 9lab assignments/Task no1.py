# Task 1

class Employee:
    def get_data(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.salary = float(input("Salary: "))
        self.address = input("Address: ")

    def show_data(self):
        print(self.name, self.age, self.salary, self.address)


class Manager(Employee):
    pass


# Process 10 managers
for i in range(2):   # change to 10 if needed
    print("\nManager", i+1)
    m = Manager()
    m.get_data()
    m.show_data()