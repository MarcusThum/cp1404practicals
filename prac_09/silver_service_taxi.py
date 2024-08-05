
from taxi import Taxi

class SilverServiceTaxi(Taxi):

    flag_fall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        self.fanciness = fanciness
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flag_fall}"
