
from silver_service_taxi import SilverServiceTaxi
def main():
    silver_service_taxi = SilverServiceTaxi("Car", 200, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(f"${silver_service_taxi.get_fare()}")

main()