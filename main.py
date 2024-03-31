from domain.Car import Car

from main_copy import print_menu
from service.services import Service
from UI.UI import UI

service = Service()
ui = UI(service)

ui.drive()
    # most_common = ''
    # brand_list = compose_brand_list(car_list)
    # max_popularity = int(-1)
    #
    # for i in range(len(brand_list)):
    #     popularity = int(0)
    #
    #     for j in range(len(car_list)):
    #
    #         if brand_list[i] == car_list[j].get_brand():
    #             popularity += 1
    #             most_common = brand_list[i]
    #
    #     if popularity > max_popularity:
    #         max_popularity = popularity
    #         most_common = brand_list[i]
    #
    # print(most_common)


def drive(plate_number=None):
    car_list = [Car(2345, 'BMW', 235, 15000),
                Car(1234, 'Toyota', 235, 15000),
                Car(555, 'Toyota', 235, 20000),
                Car(111, 'Jaguar', 235, 10000),
                Car(222, 'Toyota', 235, 40000)]
    while True:
        print_menu()
        try:
            command = int(input(" Chose the command: ").strip())
            if command == 0:
                return
            elif command == 1:
                add_car(car_list)
            elif command == 2:
                remove_car(car_list)
            elif command == 3:
                average_car_mileage(car_list)
            elif command == 4:
                most_common_brand(car_list)
            elif command == 5:
                show_car_list(car_list)
        except:
            print(" Make sure to enter one 'int' type character!")


drive()
