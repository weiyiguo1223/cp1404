
from prac_08.unreliable_car import UnreliableCar


def main():

    car_one = UnreliableCar("Good",100 ,80)
    car_two = UnreliableCar("Bad", 100, 30)

    for i in range(1, 35, 5):
        print(f"Driving distances {i}km")
        print(f"{car_one.name} drove {car_one.drive(i)}km")
        print(f"{car_two.name} drove {car_two.drive(i)}km")

    print(car_one)
    print(car_two)

main()