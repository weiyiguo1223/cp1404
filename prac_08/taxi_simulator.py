
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
def main():
    choose_taxi = ""
    total_bills = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").capitalize()
    while choice != "Q":
        if choice =="C":
            print("Taxis available: ")
            print_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))

            try:
                choose_taxi =taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif choice =="D":

            if choose_taxi != "":
                print(choose_taxi)
                choose_taxi.start_fare()
                distance = float(input("Drive how far? "))
                choose_taxi.drive(distance)
                single_trip_cost = choose_taxi.get_fare()
                print(f"Your {choose_taxi.name} trip cost you ${single_trip_cost:.2f}")
                total_bills += single_trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bills:.2f}")
        print(MENU)
        choice = input(">>> ").capitalize()
    print(f"Total trip cost: ${total_bills:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)

def print_taxis(taxis):
    number = 0
    for taxi in taxis:

        print(f"{number} - {taxi}")
        number += 1

main()
