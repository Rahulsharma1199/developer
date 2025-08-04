class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 5
        return f"Accelerating... Speed is now {self.speed} km/h"

    def brake(self):
        self.speed = max(0, self.speed - 5)
        return f"Braking... Speed is now {self.speed} km/h"

    def honk(self):
        return "Beep beep!"

    def description(self):
        return f"{self.year} {self.color} {self.make} {self.model}, Speed: {self.speed} km/h"

# Example usage:
car1 = Car("Toyota", "Camry", 2022, "Red")
print(car1.description())
print(car1.accelerate())
print(car1.accelerate())
print(car1.brake())
print(car1.honk())
