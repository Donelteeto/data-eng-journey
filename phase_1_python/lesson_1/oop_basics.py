class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary = self.salary + amount
        print(f"{self.name} received a raise! New salary: {self.salary}")

old_employee = Employee("John", 2000)
old_employee.give_raise(7000)

new_employee = Employee("Sandra", 3000)
new_employee.give_raise(5000)
