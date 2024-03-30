from main_copy import compose_distinctive_brand_list
from entities import Car
from exceptions import CustomException


class Service:
    def __init__(self):
        self.__car_list = [Car(2345, 'BMW', 235, 15000),
                           Car(1234, 'Toyota', 235, 15000),
                           Car(555, 'Toyota', 235, 20000),
                           Car(111, 'Jaguar', 235, 10000),
                           Car(222, 'Toyota', 235, 40000)]

    def get_all_cars(self):
        return self.__car_list

    def get_car(self, plate_number):
        for car in self.__car_list:
            if car.get_plate_number() == plate_number:
                return car

    def add_car(self, new_car: Car):
        plate_number = int(input("Plate number: "))
        brand = str(input("Brand: "))
        hp = int(input("Horse power: "))
        mileage = int(input("Mileage: "))
        for car in self.__car_list:
            if car == new_car:
                raise CustomException(f'The car {new_car} already exists')
            self.__car_list.append(new_car)

    def remove_car(self, car_to_delete):
        car_position = self.__get_car_position(car_to_delete)
        if car_position is not None:
            raise CustomException(f'The car {car_to_delete} already exists')
        del self.__car_list[car_position]

    def __get_car_position(self, car_to_delete):
        for i in range(len(self.__car_list)):
            if self.__car_list[i] == car_to_delete:
                return 1

        return None

    def average_car_mileage(self):
        sum_of_mileage = 0
        for car in self.__car_list:
            sum_of_mileage += car.get_mileage()
        average_mileage = sum_of_mileage / len(self.__car_list)

    def compose_distinctive_brand_list(self):
        brand_list = []
        for i in range(len(self.__car_list)):
            try:
                brand_list.index(self.__car_list[i].get_brand())
            except:
                brand_list.append(self.__car_list[i].get_brand())

        return brand_list

    def most_common_brand(self):
        brand_list = compose_distinctive_brand_list(self.__car_list)
        popularity = []
        for brand in brand_list:
            count = 0
            for a in self.__car_list:
                if brand == a.get_brand():
                    count += 1
            popularity.append({'brand': brand, 'count': count})
        # print(popularity)
        # popularity.sort(reverse=True, key=myFunc)
        # print(popularity)
        # print(popularity[0]['brand'])
