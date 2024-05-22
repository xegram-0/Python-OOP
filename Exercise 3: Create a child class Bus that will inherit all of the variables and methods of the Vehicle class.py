# Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

# Expected Output:

# Vehicle Name: School Volvo Speed: 180 Mileage: 12


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):

    def display(self):
        print(f"Vehicle name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")

schoolBus = Bus("School bus 09", 100, 30000)
schoolBus.display()