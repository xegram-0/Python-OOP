# Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class 
# with max_speed and mileage instance attributes.



class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def info(self):
        print(f"The max speed is {self.max_speed}")
        print(f"The mileage is {self.mileage}")



car = Vehicle(200, 40000)
car.info()