class Car:
    """
    Task 1: Define the Car class and its attributes.
    """
    def __init__(self, make, model, year):
        # We use 'self' to attach these values to the specific object being created
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # We access the attributes using 'self.attribute_name'
        print(f"{self.year} {self.make} {self.model}")


# Task 2: Create an instance and call the method
my_car = Car("Toyota", "Corolla", 2020)
my_car.describe_car()