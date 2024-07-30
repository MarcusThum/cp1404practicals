from car import Car

import random

class UnreliableCar:


    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.car = Car(self.name, self.fuel)

    def drive(self, distance):
        random_int = random.randint(1, 100)
        if random_int < self.reliability:
            return self.car.drive(distance)
