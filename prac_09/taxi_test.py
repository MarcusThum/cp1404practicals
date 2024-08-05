
from taxi import Taxi
def main():
    taxi = Taxi("Prius 1", 100)
    taxi.start_fare()
    taxi.drive(40)

    print(f"${taxi.get_fare()}")
    print(taxi)

    taxi.start_fare()
    taxi.drive(100)

    print(f"${taxi.get_fare()}")
    print(taxi)

main()