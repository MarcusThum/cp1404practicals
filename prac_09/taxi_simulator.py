from silver_service_taxi import SilverServiceTaxi

from taxi import Taxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("q)uit, c)hoose taxi, d)rive")

    menu_input = input(">>> ")

    loop = True

    choice = -1

    taxi_fare = 0

    while loop:
        if menu_input.lower() == "c":
            choice = choose_taxi(taxis)
            print(f"Bill to date: ${taxi_fare:.2f}")
            menu_input = ""
        if menu_input.lower() == "d":
            taxi_fare += drive(taxis, choice)
            print(f"Bill to date: ${taxi_fare:.2f}")
            menu_input = ""
        if menu_input.lower() == "q":
            loop = False
        else:
            print("q)uit, c)hoose taxi, d)rive")
            menu_input = input(">>> ")

def drive(taxis, choice):

    distance_drive = 0

    if choice == -1:
        print("Taxi not Choosen")
    else:
        distance_drive = input("Drive how far? ")
        boolean = True
        while boolean:
            try:
                if int(distance_drive) < 0:
                    print("Invalid Distance")
                    distance_drive = input("Drive how far? ")
                else:
                    boolean = False
            except ValueError:
                print("Invalid Distance")
                distance_drive = -1

    taxis[choice].drive(int(distance_drive))
    print(f"${taxis[choice].get_fare():.2f}")

    return taxis[choice].get_fare()



def choose_taxi(taxis):
    print("Taxis available: ")
    for i in range(0, len(taxis)):
        print(f"{i} - {taxis[i]}")

    taxi_choice = input("Choose taxi: ")
    boolean = True
    while boolean:
        try:
            if int(taxi_choice) < 0 or int(taxi_choice) >= len(taxis):
                print("Invalid Taxi Choice")
                taxi_choice = input("Choose taxi: ")
            else:
                boolean = False
        except ValueError:
            print("Invalid Taxi Choice")
            taxi_choice = -1

    return int(taxi_choice)


main()