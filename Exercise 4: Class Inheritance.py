# Exercise 4: Class Inheritance
# Given:

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# Expected Output:

# The seating capacity of a bus is 50 passengers

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        # This does nothing to the overall result
        #self.capacity = 50
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    # def seating_capacity(self, capacity=50):
    #     return super().seating_capacity(capacity=50)
    

schoolBus = Bus("School Bus 09", 100, 30000)
# This passing the value to the method but not the as a default value
#print(schoolBus.seating_capacity(50))

# This however, can
print(schoolBus.seating_capacity())
