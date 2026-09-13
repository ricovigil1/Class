class Car:
    def __init__(self, speed):
        self.speed = speed

    def calculate_distance(self, time):
        return self.speed * time


# Create a Car object with an integer speed of 70 mph.
car = Car(70)

# Time and calculated distance are also integers.
for hours in (6, 10, 15):
    distance = car.calculate_distance(hours)
    print(f"In {hours} hours, the car will travel {distance} miles.")
