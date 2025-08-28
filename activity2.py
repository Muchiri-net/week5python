

class Vehicle:
    def move(self):
        pass  # Each vehicle defines its own move behavior


# Derived classes
class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is pedaling forward 🚲")

class Car(Vehicle):
    def move(self):
        print("Car is driving on the road 🚗")


# Test 
vehicles = [Bicycle(), Car()]

print("Activity 2: Vehicles moving differently")
for v in vehicles:
    v.move()
