from main import service
from domain.Car import Car
from domain.exceptions import CustomException


class UI:
    def __init__(self):
        self.__service = service

    def __print_menu(self):
        print("1. Add car")
        print("2. Delete car")
        print("3. Average car mileage")
        print("4. Most common brand")
        print("5. Show car list")
        print("0. Exit menu")

    def __show_car_list(self):
        for car in self.__service.get_all_cars():
            print(car)

    def __add_car(self, car_list):
        plate_number = int(input("Plate number: "))
        brand = str(input("Brand: "))
        hp = int(input("Horse power: "))
        mileage = int(input("Mileage: "))
        self.__service.add_car(Car(int(plate_number), brand, hp, mileage))
        print('Car added to the list!')

    def validate_plate_number(self, plate_number):
        try:
            int(plate_number)
        except ValueException:
            raise CustomException('Car plate number is not a number!')

    def average_car_mileage(self):
        average_mileage = self.__service.average_car_mileage()
        print(f'The average car mileage in the TAXI company is {average_mileage}')

    def __remove_car(self):
        plate_number = input("Car to delete plate number: ")
        self.__service.remove_car(Car(int(plate_number)))
        print('Car deleted!')
            
    def drive(self, car_list):

        while True:
            self.__print_menu()
            try:
                command = int(input(" Chose the command: ").strip())
                if command == 0:
                    return
                elif command == 1:
                    self.__add_car(car_list)
                elif command == 2:
                    self.__remove_car(car_list)
                elif command == 3:
                    self.__average_car_mileage(car_list)
                elif command == 4:
                    self.__most_common_brand(car_list)
                elif command == 5:
                    self.__show_car_list(car_list)
            except CustomException as error:
                print(error)
                
