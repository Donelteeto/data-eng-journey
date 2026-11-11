class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"This is a {self.brand} going {self.speed} mph")

class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_size):
        super().__init__(brand, speed)
        self.battery_size = battery_size

    def charge(self):
        print(f"{self.brand} is charging. Battery: {self.battery_size} kwh")

    def __str__(self):
        return f"{self.brand} (Electric) - {self.speed} mph"

car = ElectricCar("Tesla", 180, 50)

car.describe()
car.charge()
print(car)