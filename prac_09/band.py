
from musician import Musician

class Band(Musician):
    def __init__(self, band):
        super().__init__()
        self.band = band
        self.musicians = []

    def __str__(self):
        return f"{self.band} ({self.musicians})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musicians):
        self.musicians.append(musicians)

    def play(self):
        for i in range(0, len(self.musicians)):
            print(f"{self.musicians[i]}")


